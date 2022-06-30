#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 23:33:01 2022

@author: cian
"""

netIncome = int (input("請輸入今年收入淨額："))
if (netIncome >=300000):
    if (netIncome >=2000000):
        print ("付稅金額：" + str(netIncome * 0.3), end = " 元")
    elif (netIncome in range(1000000, 1999999)):
        print ("付稅金額：" + str(netIncome * 0.21), end = " 元")
    elif (netIncome in range(600000, 999999)):
        print ("付稅金額：" + str(netIncome * 0.13), end = " 元")
    elif (netIncome in range(300000, 599999)):
        print ("付稅金額：" + str(netIncome * 0.06), end = " 元")
else:
    print ("付稅金額：" + str(netIncome * 0), end = " 元")