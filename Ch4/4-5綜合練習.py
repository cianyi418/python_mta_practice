#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:22:35 2022

@author: cian
"""

num = int (input("請輸入正整數："))
yinshu = []
for n in range(1, num+1):
    # while True:
    if num % n == 0:
        yinshu.append(n)

print(str(num) + "的因數有 ")
print(list(yinshu))


if len(yinshu) > 2:
    print(str(num) + "不是質數" )
else:
    print(str(num) + "是質數")
        #print(str(num) + "的因數有 \n")
        #print(str(n), end="")
        # print("{}的因數有{}".format(num, n),end=" \n")
        #print(str(num) + "不是質數")
            # break
        # else:
           # break
        


# a = b = int (input("請輸入正整數："))
# output = ' '
# while True:
#     for i in range(2, (a+1)):
#         if a == b:
#             break
#         if a % i == 0:
#             output += f'{i}'
#             a = int(a/i)
#             break
#     if a == 1 or a == b:
#         break
#     else:
#         output += "*"
# if a == b:
#     print(f'{b}是質數')
# else:
#     print(f'{b} = {output}')


