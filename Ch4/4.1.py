#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:01:49 2022

@author: cian
"""

num = int (input("請輸入正整數："))
# if (num % 2) == 0:
#     odd = filter(lambda n: n % 2 == 1, range(1, num+1))
#     print(list(odd))

for n in range(1, num+1):
    if (n % 2) != 0:
        print(n) 