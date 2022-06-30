#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 21:59:41 2022

@author: cian
"""
weather = str (input("今天會下雨嗎？"))
# def weather(s):
#     return s.lower()
if weather.lower() == "y":
    print("出門請帶傘！")
else:
    print("")