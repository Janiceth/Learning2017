# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘PyTest’
from logging import exception

import Excel
import xlwt
import os, sys
import  xml.dom.minidom as xx
import xml.etree.ElementTree as  ET  # 引入解析xml的方法

xmlfile =u'./幻视APP测试用例-3.11.xml'


def print_node(node):
    ''''打印节点基本信息'''
    print "=================================================="
    print "node.attrib:%s" % node.attrib
    if node.attrib.has_key("name") > 0 :
        print "node.attrib['name']:%s" % node.attrib['name']
    print "node.tag:%s" % node.tag
    print "node.text:%s" % node.text


# 读取xml文件
try:
    tree = ET.parse('E:\\Learning\\Outcomes\\XmlToExcel\\src\\EyegicAPP Testcase-3.11.xml')  # 载入数据
    root = tree.getroot()     # 获取根节点
except exception, e:
    print "Error:cannot parse file:幻视APP测试用例-3.11.xml"
    sys.exit(1)

print root.tag, "---",root.attrib
for child in root:
    print child.tag, "---",child.attrib

print "*"*10
print root[0][1].text   #  通过下标访问
print root[0].tag, root[0].text
print "*"*10

for testcase in root.findall('testcase'):    # 找到root节点下所有的testcase节点
    name = testcase.get('name')     #子节点下属性name的值
    importance = testcase.find('importance').text
    summary = testcase.find('summary').text   # 子节点下节点summary的值
    preconditions = testcase.find('preconditions').text   # 子节点下预置条件的值

    print name, importance, summary, preconditions









