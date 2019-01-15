# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’

# !/usr/bin/env python

'makeTextFile.py --create text file'

import os
ls = os.linesep

# get filename
fname = raw_input('Enter filename:')
while True:


    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

    # get file content (text) lines

all = []
print("\nenter lines ('.' by iteself to quit).\n")

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' %(x, ls) for x in all])
fobj.close()
print("done!")