#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 23:16:53 2022

@author: cian
"""

numbers2 = []
numbers = [1, 2, 3, 4, 2, 7, 3, 2, 3]
for num in numbers:
    n = numbers2.count(num)
    if n ==0:
        numbers2.append(num)
print(numbers2)