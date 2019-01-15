# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘src’


import os
import glob
import os.path

Const_File_Format = [".jpg", ".png", ".txt", ".jpeg", ".bmp", ".gif"]
rootDir = "e:\TestPython"

os.path.exists(folderpath.encode('GBK'))  # 如果路径存在，返回TRUE
limit_size = 1

class FileFilt:
    counter = 0
    deleted = 0
    errord = 0
    def __init__(self):
        pass

    def FilterFile(self,dir):
        for parent, dirnames, filenames in os.walk(rootDir):
            for dirname in dirnames:
                print "dirname is:" + dirname
                print "parent is:" + parent
            for filename in filenames:
                fileDir = os.path.join(parent, filename)
                if fileDir and (os.path.splitext(fileDir)[1] in Const_File_Format):
                    filesize = os.path.getsize(fileDir)
                    if(filesize <= limit_size):
                        os.remove(fileDir)
                        self.delete += 1
                    else:
                        try:
                            fp = open(fileDir, 'rb')

