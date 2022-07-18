#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:03:15 2022

@author: cian
"""

airQuality = {"台北市" : 6, "新北市" : 2, "桃園市" : 5, "台中市" : 8, "台南市" : 3, "高雄市" : 9}
city = (input("輸入要查詢的六都名稱："))
PM = airQuality.get(city)
if PM == None:
    print("六都中沒有「" + city + "」城市！")
else:
    
# if city in airQuality:
    print(city + "今天的 PM2.5 值為：" + str(airQuality[city]))