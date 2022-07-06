#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:16:26 2022

@author: cian
"""

sum = 0
for i in range (1,100):
    if (i % 3 ==0 or i % 7 ==0):
        sum += i
print("數值 1~100 中，所有是 3 或 7 倍數的數之總和 = " + str(sum))