#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#! python3
#
#  language.py
#  
#  Copyright 2014 Ben Klein <robobenklein@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
# For use with life.py
#

import random
import language_tool
import subprocess
try:
    import ginger
except:
    pass

# End imports, begin init

print("------------Language Module initializing------------")

dictionary = "soul_data/dictionary.txt"

with open(dictionary) as myfile:
    wordCount = sum(1 for line in myfile)
    
print("You have " + str(wordCount) + " words available to match.")

print("------------Language Module initialized-------------")

# End init, Begin function definitions

def getRandomWords(WordCount, returnList = False):
    wordlist = []
    while not (len(wordlist) == WordCount):
        wordlist.append(getRandomWord())
    if returnList == False:
        return "".join(wordlist).replace("\n", " ")
    else:
        return wordlist

def getRandomWord():
    #Open englishWords.txt and get a random line from it.
    with open(dictionary) as fp:
        wordNum = random.randint(1, wordCount)
        for i, line in enumerate(fp):
            if i == wordNum:
                return line
            elif i > wordNum:
                break
    

def getSentiment(sentence):
    pass

def verifyText(sentence, method = "langtool"):
    if method == "langtool":
        target = open('text.txt', 'w')
        target.write(sentence)
        target.close()
        data = subprocess.check_output("java -jar langTool/languagetool-commandline.jar -l en-US -d MORFOLOGIK_RULE_EN_US text.txt", shell=True)
        num_lines = len(data.splitlines())
        # Enable to debug
        #print(data)
        #print(num_lines)
        if num_lines >= 4:
            #print("Sentence invalid.")
            return False
        else:
            #print("Sentence VALID: " + sentence)
            return True
    if method == "ginger":
        if ginger.check(sentence) == 0:
            return True
        else:
            return False

def formatSentence(sentence):
    sentence = sentence.capitalize()
    sentence = sentence.strip() + "."
    return sentence
    
