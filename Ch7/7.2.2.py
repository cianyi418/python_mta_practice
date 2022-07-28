#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:12:44 2022

@author: cian
"""

livingExpense = 10000
dailySpend = 350
ret = divmod(livingExpense, dailySpend)
print("可維持生活 " + str(ret[0]) + " 天")
print("生活費剩餘 " + str(ret[1]) + " 元")