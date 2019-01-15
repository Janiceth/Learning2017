# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’


# 字符串（string）和文本
x = "There are %d types of people." % 10
binary = "Binary"
do_not = "don't"
y = "Those who kown %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I alse said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a stting with a right side."
print w + e
