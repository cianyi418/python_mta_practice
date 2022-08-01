#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 22:47:33 2022

@author: cian
"""


listName = ("鍾明達", "鄭廣月", "何美麗")
listQ1 = (34210, 23600, 145000)
listQ2 = (9000, 23900, 83400)
listQ3 = (186500, 127800, 100000)
listQ4 = (78900, 125000, 90000)
print("姓名".ljust(5), "第一季".center(10), "第二季".center(4), "第三季".center(7), "第四季".center(5))
for i in range(0,3):
    print(listName[i].ljust(5), str(listQ1[i]).rjust(8), str(listQ2[i]).rjust(8), str(listQ3[i]).rjust(8), str(listQ4[i]).rjust(8))