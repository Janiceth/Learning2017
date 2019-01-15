# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘XmlToExcel’


# 转换 “幻视APP自动化基线测试用例.testsuite-deep.xml”

import xml.etree.ElementTree as ET

xmlfile = u'幻视APP自动化基线测试用例.testsuite-deep.xml'
tree = ET.parse(xmlfile)
# 获取 xml 根目录
root = tree.getroot()
# 获取 测试用例集
testsuite_per = root.findall("testsuite")
# 循环测试用例集
aa = {}
dict_temp = {}
xe = xml_excel()

for num_suite in range(0, len(testsuite_per)):
    xe.write_heard(testsuite_per[num_suite].get('name'))
    # 获取子用例集
    row_flag = 1
    list_row = [0]
    for testsuite_son in testsuite_per[num_suite].findall("testsuite"):
       # 获取测试用例
        testcase = testsuite_son.getiterator("testcase")
        num = len(testcase)
        #  print num
        # 循环每个测试用例
        for case in range(0, num):
            steps=testcase[case].getiterator('step')
           # 循环测试用例步骤
            for step in steps:
                list_temp=[]
                list_temp.append(step[1].text)
                list_temp.append(step[2].text)
                dict_temp[step[0].text]=list_temp
                # aa['step']=dict_temp
            # print dict_temp,len(steps),row_flag
            row_start = row_flag
            if len(steps) != 0:
                for i in range(1, len(steps) + 1):
                    xe.write_count(row_flag, 4, str(i))
                    if dict_temp[str(i)][0] != None:
                        xe.write_count(row_flag, 5, xe.excel_replace(dict_temp[str(i)][0]))
                    else:
                        xe.write_count(row_flag, 5, dict_temp[str(i)][0])
                    if dict_temp[str(i)][1] != None:
                        xe.write_count(row_flag, 6, xe.excel_replace(dict_temp[str(i)][1]))
                    else:
                        xe.write_count(row_flag, 6, dict_temp[str(i)][1])
                    row_flag = 1
            else:
                row_flag = 1
                continue

            # xe.excel_merge(row_start,row_flag-1,0,0)
            xe.excel_merge(row_start, row_flag-1, 1, 1, testcase[case].get('name'))
            if testcase[case].find('summary').text != None:
                xe.excel_merge(row_start, row_flag-1, 2, 2, xe.excel_replace(testcase[case].find('summary').text))
            else:
                xe.excel_merge(row_start, row_flag-1, 2, 2, testcase[case].find('summary').text)
            if testcase[case].find('preconditions').text != None:
                xe.excel_merge(row_start, row_flag-1, 3, 3, xe.excel_replace(testcase[case].find('preconditions').text))
            else:
                xe.excel_merge(row_start, row_flag-1, 3, 3, testcase[case].find('preconditions').text)
        list_row.append(row_flag-1)
        # print list_row
        # print list_row[len(list_row)-1],list_row[len(list_row)-2]
        if num != 0:
            xe.excel_merge(list_row[len(list_row)-2] + 1, list_row[len(list_row)-1], 0, 0, testsuite_son.get('name'))
        else:
            continue
        xe.cell_width()
        xe.save_excel()
                # xe.write_merge(aa)
print '转转换完毕 请查阅'
