#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:11:43 2022

@author: cian
"""

def kgTolb(kg):
    lb = kg * 2.2
    return lb
inputKg = float(input("請輸入體重公斤數："))
print("你的體重為： %.2f 磅" % kgTolb(inputKg))