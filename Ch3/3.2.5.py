#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:58:22 2022

@author: cian
"""

a = int (input("請輸入 a 的值："))
b = int (input("請輸入 b 的值："))
c = int (input("請輸入 c 的值："))

# maximum = max(a,b,c)
# print("最大值為：" + str(maximum))

def maxnum (a,b,c):
    if a > b:
        return a
    elif a > c:
        return a
    elif b > a:
        return b
    elif b > c:
        return b
    elif c > a:
        return c
    elif c > b:
        return c
print ("最大值為：" + str (maxnum (a,b,c)))
        
    