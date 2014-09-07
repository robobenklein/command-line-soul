#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#! python3
#
#  life.py
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
# life.py is meant to hold soul.py and language.py
#
# This code is an Experiment on Artificial Intelligence.
#
# Project started Sept. 5th 2014
#
# 4 Spaces for one Indent
#
'''

v/ Generate random sets of words between 2 and some number of words. (Get list of words from .txt)
v/ Automatically remove the sentences that didn't pass a grammer check. (NLTK or some analysis)
[] Record sentences and responses. (MongoDB?)
[] Identify sentiment comparison for each combination (Sentiment Analysis)



'''


import random
import language

#! XKCD Reference Achieved
import soul
#!

def main():
    
    sentence = language.formatSentence(language.getRandomWords(random.randint(2, 6)))
    #print(sentence)
    if language.verifyText(sentence, "ginger"):
        print("------<==== VALID ====>------")
        print(sentence)
    else:
        print("------<====INVALID====>------")
        print(sentence)

while 1:
    main()
    print("---------------------------------------")
    
