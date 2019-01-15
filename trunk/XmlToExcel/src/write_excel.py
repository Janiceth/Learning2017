# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘XmlToExcel’

import xlwt
import re
import os
class write_excel():
    def __init__(self):
        self.file = xlwt.Workbook(encoding='UTF-8')
        self.borders = xlwt.Borders()
        self.pattern = xlwt.Pattern()
        self.font = xlwt.Font()
        self.style = xlwt.XFStyle()

    def sheet_border(self):
        # 设置边框
        self.borders.left = xlwt.Borders.THIN
        self.borders.right = xlwt.Borders.THIN
        self.borders.top = xlwt.Borders.THIN
        self.borders.bottom = xlwt.Borders.THIN
        self.style.borders = self.borders
        return self.style

    '''def sheet_font(self):
        self.font.name='SimSun'
        self.font.bold=True
        self.style.font=self.font'''



    def write_heard(self, name1):
        self.add_shet = self.file.add_sheet(name1)
        self.add_shet.write(0, 0, '用例名称', self.sheet_border())
        self.add_shet.write(0, 1, '用例等级', self.sheet_border())
        self.add_shet.write(0, 2, '执行方式', self.sheet_border())
        self.add_shet.write(0, 3, '关键字', self.sheet_border())
        self.add_shet.write(0, 4, '用例摘要', self.sheet_border())
        self.add_shet.write(0, 5, '预置条件', self.sheet_border())
        self.add_shet.write(0, 6, '操作步骤', self.sheet_border())
        self.add_shet.write(0, 7, '预期结果', self.sheet_border())
        self.add_shet.write(0, 8, '测试方式', self.sheet_border())
        self.add_shet.write(0, 9, '规约编号', self.sheet_border())

    # 写数据
    def write_count(self, num1, num2, str1):
        self.add_shet.write(num1, num2, str1, self.sheet_border())

    # 合并单元格
    def excel_merge(self, num11, num22, num33, num44, str11):
        self.add_shet.write_merge(num11, num22, num33, num44, str11, self.sheet_border())

    # 设置单格宽高
    def cell_width(self):
        self.add_shet.col(0).width = 5000
        self.add_shet.col(1).width = 1500
        self.add_shet.col(2).width = 1000
        self.add_shet.col(3).width = 1500
        self.add_shet.col(4).width = 5000
        self.add_shet.col(5).width = 7000
        self.add_shet.col(5).height = 6000
        self.add_shet.col(6).width = 10000
        self.add_shet.col(6).height = 6000
        self.add_shet.col(7).width = 9000
        self.add_shet.col(7).height = 6000
        self.add_shet.col(8).width = 7000
        self.add_shet.col(9).width = 7000

    # 保存Excel
    def save_excel(self):
        self.file.save('幻视APP自动化基线测试用例.xls')

    # 替换xml符号标识
    def excel_replace(self, ss):
        self.re_cdata = re.compile('</{ 0,1 }[^>]*>', re.I)
        self.s = re.compile(r'&')
        # & 符号
        self.re_ca = re.compile(r'&')
        # 小于号
        self.re_cx = re.compile(r'<')
        # 大于号
        self.re_cd = re.compile(r'>')
        # 双引号
        self.re_cs = re.compile(r'"')
        # 空格
        self.re_ck = re.compile(r' ')
        # 破折号
        self.re_cp = re.compile(r'—')
        # 上尖括号;
        self.re_cj = re.compile(r'…')
        # 中文双引号
        self.re_czsl = re.compile(r'“')
        # 中文双引号
        self.re_czsr = re.compile(r'”')
        # 中文单引号
        self.re_czdl = re.compile(r'‘')
        # 中文单引号
        self.re_czdr = re.compile(r'’')
        s = self.re_cdata.sub('', ss)
        s = self.re_ca.sub(r'&', s)
        s = self.re_cx.sub(r'<', s)
        s = self.re_cd.sub(r'>', s)
        s = self.re_cs.sub(r'"', s)
        s = self.re_ck.sub(r' ', s)
        s = self.re_cp.sub(r'-', s)
        s = self.re_cj.sub(r'^', s)
        s = self.re_czsl.sub(r'“', s)
        s = self.re_czsr.sub(r'”', s)
        s = self.re_czdl.sub(r'‘', s)
        s = self.re_czdr.sub(r'’', s)
        return s
    def set_merge(self):
        pass



if __name__ == "__main__":
    current_dir = os.getcwd()
    case_dir_xml = current_dir + "\\resource\\testcases.xml"
    case_dir_excel = current_dir + "\\resource\\testcases.xls"
    print case_dir_excel
    wr = write_excel(case_dir_xml)
    wr.write_title()
    wr.write_content()
    wr.save_excel(case_dir_excel)