#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:52:55 2022

@author: cian
"""
for i in range (2,10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%2d " % (i, j, product), end="")
    print()