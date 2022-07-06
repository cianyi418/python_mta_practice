#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:44:52 2022

@author: cian
"""

even = 1
num = int (input("請輸入正整數 n 的值："))
while even <= num:
    if (even % 2) == 0:
        print (even)
    even += 1

