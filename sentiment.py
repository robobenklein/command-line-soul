#!/usr/bin/env python
# -*- coding: utf-8 -*-
#! python
#
#  sentiment.py
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
# This file is to let python3 run these old python2 sentiment analyses
#

#Because this file should appear to hold the functions itself.
#Runs on an older version of python...
from past import autotranslate
autotranslate('sentiment_analysis')
from sentiment_analysis import * 

from basic_sentiment_analysis import *
