#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:20:40 2022

@author: cian
"""

chineseZodiac = {"鼠" : "親切和藹", "牛" : "保守努力", "虎" : "熱情大膽", "兔" : "溫柔仁慈"} 
characterIterm = chineseZodiac.items()
for zodiacAnimal, character in characterIterm:
    print("生肖屬 %s 性格特徵為 %s" % (zodiacAnimal, character))