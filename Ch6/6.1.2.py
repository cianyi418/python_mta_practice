#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:51:48 2022

@author: cian
"""

fourSeason = {"春季" : "舒適", "夏季" : "酷熱", "秋季" : "涼爽", "冬季" : "寒冷"}
name = input("輸入季節名稱：")
season = fourSeason.get(name)
if season == None:
    print("沒有「" + name + "」季節！")
else:
    print(name + "的天氣為 " + str(fourSeason[name]))
