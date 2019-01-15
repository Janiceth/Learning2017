# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

"""判断正负数.

主要功能描述.

  ClassFoo: 类概述.
  functionBar(): 函数概述.
"""
import re
import string


num = '^[-+]{0,1}[0-9]{1,}.{0,1}[0-9]{0,}'
check = True
while check:
    input = raw_input("请输入一个数值：")
    if len(input) == 0 or not re.findall(num,input):
        print "程序退出！"
        break
    inputnew = string.atof(input)
    if inputnew > 0 or inputnew < 0:
        if inputnew > 0:
            print input , "是正数！"
        if inputnew < 0:
            print input , "是负数！"
    else:
        print "输入的是0，既不是正数也不是复数！"
