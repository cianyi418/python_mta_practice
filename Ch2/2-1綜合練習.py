#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 00:02:39 2022

@author: cian
"""
student1 = str (input("請輸入第一位同學的姓名："))
score1 = int (input("請輸入第一位同學的成績："))
student2 = str (input("請輸入第二位同學的姓名："))
score2 = int (input("請輸入第二位同學的成績："))

print ("姓名  " + "  成績")
print ("{0:2s} {1:-4d}".format(student1, score1))
print ("{0:2s} {1:-4d}".format(student2, score2))
print ("總成績為：" + str(score1 + score2))