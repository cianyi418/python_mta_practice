#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:43:49 2022

@author: cian
"""

fee = 70
distance = int (input("請輸入路程公里數（整數）："))
fee += (distance - 1) *30
print ("你的車程車資費用為：" + str(fee))