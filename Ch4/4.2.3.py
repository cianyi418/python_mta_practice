#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:17:49 2022

@author: cian
"""

num = int ( input("請輸入大樓的樓層數："))
print ("本大樓具有的樓層為：")
for floor in range (1, num+1):
    if floor ==4:
        continue
    print((floor), " ", end="")
    