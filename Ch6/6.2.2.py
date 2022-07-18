#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:39:31 2022

@author: cian
"""

priceList = {"電視" : 15000, "冰箱" : 23000, "冷氣" : 28000}
productName = str(input("輸入電器名稱："))
if productName in priceList:
    print(productName + "的價格為 " + str(priceList[productName]))
else:
    price = int(input("輸入電器價格："))
    priceList[productName] = price
    print("字典內容：" + str(priceList))