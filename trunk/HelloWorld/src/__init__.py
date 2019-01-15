# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

import sys

user = raw_input('enter login name:')
print 'Your login is:', user

logfile = open('E:/Learning/Outcomes/Hello World/src/helloworldlong.txt', 'a')
print >>sys.stderr, 'Fatal error:invalid input!'
logfile.close()

# print "%s is number %d!" % ("Python", 1)
# myString = 'Hello World!'
# print myString



