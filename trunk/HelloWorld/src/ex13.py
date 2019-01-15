# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

from sys import argv  # 导入sys模组（或者叫库）

# 将argv解包，将每个参数赋予一个变量
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your third variable is:", argv
