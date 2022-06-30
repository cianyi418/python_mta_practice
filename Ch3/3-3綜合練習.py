#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 23:18:51 2022

@author: cian
"""

month = int (input("請輸入月份："))
if month in range(1, 3):
    print (str(month) + " 月是春天！")
elif month in range(4, 6):
    print (str(month) + " 月是夏天！")
elif month in range(7, 9):
    print (str(month) + " 月是秋天！")
else:
    print (str(month) + " 月是冬天！")