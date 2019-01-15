# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘EyegicAPPTest’

import os

file = open('./Momo.py', 'w')
file.write("Hello Python")
file.close()

for i in range(1, 20, 3):
    if i == 16:
        break
    elif i % 2 == 0:
        print("我是偶数：" + str(i))
    else:
        print("我是奇数：" + str(i))
else:
    print("for循环结束")

