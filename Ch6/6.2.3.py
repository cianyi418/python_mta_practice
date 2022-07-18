#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:05:20 2022

@author: cian
"""

fourConstellations = {"水瓶座" : "活潑善變", "雙魚座" : "迷人保守", "白羊座" : "天生勇者", "金牛座" : "熱情敏感"}
constellationList = list(fourConstellations.keys())
character = list(fourConstellations.values())
for i in range(len(constellationList)):
    print(" %s 的性格特徵為 %s" % (constellationList[i], character[i]))