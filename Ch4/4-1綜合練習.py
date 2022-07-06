#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:32:07 2022

@author: cian
"""

sum = 0
for i in range(1, 100, 2):
    if (i % 2) != 0:
        sum += i
print(sum)