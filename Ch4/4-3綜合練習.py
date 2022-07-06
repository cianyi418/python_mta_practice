#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:03:02 2022

@author: cian
"""

num = int (input("請輸入正整數："))
for n in range(num, 0, -1):
    print(end="")
    for m in range(n, 0, -1):
        print("*", end="")
    print()