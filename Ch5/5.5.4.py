#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:37:40 2022

@author: cian
"""

scores = []
while True:
    inscore = input("請輸入學生的成績：")
    if (inscore ==""):
        break
    scores.append(int(inscore))
    scores.sort()
    print(scores)