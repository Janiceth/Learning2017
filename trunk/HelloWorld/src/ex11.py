# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

# 程序输入和输出
print "How old are you?",
age = raw_input()
print "How tall are you?",
# height = raw_input()
height = float(raw_input())
print "How much do you weigh?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So,you're %s old, %s tall and %s heavy." % (age, height, weight)
# print "So,you're %d old, %d tall and %d heavy." % (age, height, weight)

y = raw_input("you're name?")