# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘src’


import os
import os.path

rootdir = "e:\SVN"    # 被遍历的文件夹

for parent, dirnames, filenames in os.walk(rootdir):    #  返回父目录、所有文件夹名字、所有文件名字
    for dirname in dirnames:                         # 文件夹信息
        print "parent is:" + parent
        print "dirname is:" + dirname

    for filename in filenames:
        print "parent is:" + parent
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(parent, filename)   # 文件的路径信息