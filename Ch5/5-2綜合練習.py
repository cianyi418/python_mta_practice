#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:19:27 2022

@author: cian
"""

fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]
while True:
    fruit = input("請輸入喜歡的水果(Enter 結束):")
    if (fruit ==""):
        break
    i =fruits.count(fruit)
    if (i>0):
        n = fruits.index(fruit)
        print("%s 在串列第 %d 項" % (fruit, n+1))
    else:
        print(fruit, "不在串列中！")
    