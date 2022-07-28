#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 22:53:31 2022

@author: cian
"""

fileName = input("請輸入圖片檔案名稱：")
if fileName.endswith(".jpg") or fileName.endswith(".JPG"):
    print("圖片格式是 JPG!")
else:
    print("圖片格式不是 JPG!")