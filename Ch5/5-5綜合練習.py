#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:19:59 2022

@author: cian
"""

names = []
scores = []

for student in range(1, 4):
    names.append(input("請輸入第 {} 位同學的姓名：".format(student)))
    scores.append(int(input("請輸入第 {} 位同學的成績：".format(student))))
#     scores2 = sorted(scores, reverse = True)
# for i in range(len(scores2)):
#     print("姓名： %s  成績： %d" % (names[i], scores2[i]))
highestScore = max(scores)
idxHighestScore = scores.index(highestScore)

print("姓名： %s  成績： %d" % (names[idxHighestScore], highestScore))
