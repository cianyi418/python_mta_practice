#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 22:30:37 2022

@author: cian
"""

num = int (input("請輸入正整數："))
if (num % 2) == 0:
    print (str(num) + (" 為偶數!"))
else:
    print (str(num) + (" 為奇數！"))