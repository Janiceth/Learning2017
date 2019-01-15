# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘src’

import glob
import os
os.chdir("./")
for file in glob.glob("*.py"):
    print file

print "##########Another One##############"

for file in os.listdir("./"):
    if file.endswith(".py"):
        print file


print "##########Another Two##############"
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".py"):
            print os.path.join(root, file)


print "##########Another Three##############"

os.chdir("./")
filename_arr = {}
i = 0
for files in glob.glob("*.py"):
    filename_arr[i] = files
    i += 1

for key, value in filename_arr.items():
    print key, value