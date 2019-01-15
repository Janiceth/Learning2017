# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

# !/usr/bin/env python

'readTextFile.py ----read and display text file'

# get filename

fname = raw_input('Enter Filename:')
print


# attempt to open file for reading

try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open errror:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()