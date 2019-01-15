# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘PyTest’

# !/usr/bin/env python
def view_dir(path = '.'):
    '''
    本函数打印给定目录中的所有文件和目录
    :args path:指定目录，默认为当前目录
    :return:
    '''
    names = os.listdir(path)
    names.sort()

    form name in names:
        print(name, end = ' ')
    print()
