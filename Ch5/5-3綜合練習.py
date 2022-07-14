#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:39:18 2022

@author: cian
"""

scores = []
for student in range(1,6):
    scores.append(int(input("請輸入第 {0} 位同學的成績：".format(student))))
    total = sum(scores)
    avg = sum(scores) / len(scores)
print("本班總成績：%d 分，平均成績：%.2f 分" % (total, avg))
    