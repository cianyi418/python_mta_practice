#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:29:15 2022

@author: cian
"""

depositAmount = []
days = [1, 2, 3, 4, 5, 6, 7]
total = amount = 0

# for day in range(1,8):
#    total += int(input("Please input deposite of day {0}: ".format(day)))
# print("total: {0}".format(total))

for day in days:
    depositAmount.append(int(input("Please input deposite of day {0}: ".format(day))))
print("total: {0}".format(sum(depositAmount)))