#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:55:28 2022

@author: cian
"""

colors = ["紅", "橙", "黃", "綠", "藍"]
while True:
    print("顏色有：", colors)
    color = input("請輸入要刪除的顏色(Enter 結束):")
    if (color ==""):
        break
    n = colors.count(color)
    if (n>0):
        colors.remove(color)
    # else:
    #     break