#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:27:11 2022

@author: cian
"""

expenditure = []
for amount in range(1,5):
    expenditure.append(int(input("請輸入第 {} 個月的支出金額：" .format(amount))))
print("支出最多的金額為： %d" % max(expenditure))
print("支出最少的金額為： %d" % min(expenditure))
print("支出的總額為： %d" % sum(expenditure))
print("支出金額由小到大排序為： {}" .format(sorted(expenditure)))