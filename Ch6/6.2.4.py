#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:37:22 2022

@author: cian
"""

fourConstellations = {"水瓶座" : "活潑善變", "雙魚座" : "迷人保守", "白羊座" : "天生勇者", "金牛座" : "熱情敏感"}
characterIterm = fourConstellations.items()
for constellation, character in fourConstellations:
    print(" %s 的性格特徵為 %s" % (constellation, character))