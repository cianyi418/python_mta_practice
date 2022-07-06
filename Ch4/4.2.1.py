#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:53:30 2022

@author: cian
"""

num = int (input("請輸入正整數："))
for n in range ( 1, num+1 ):
    print(end="")
    for m in range( 1, n+1):
        print(m, end="")
    print()