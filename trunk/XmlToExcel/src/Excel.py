# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘XmlToExcel’

import xlrd
import xlwt    # xlrd 读Excel，xlwt 写Excel

class Excel:
    def __init__(self):
        self.workbook = None
        self.worksheet = None

    def open_excel(self, file):
        try:
            self.workbook = xlrd.open_workbook(file)
        except Exception,e:
            print "Error:cannot open Excel file"

    def creat_excel(self, file):
        try:
            w = xlwt.Workbook(file)
            self.workbook = w
            self.worksheet = w.add_sheet("sheet1")

        except Exception,e:
            print "Error:creat excel failed!"
            return None

    def creat_sheet(self, workbook, sheet_name="Sheet1"):
        try:
            ws = workbook.add_sheet(sheet_name)
            self.worksheet = ws
            return ws
        except Exception,e:
            print "Error:creat exccel sheet failed!"
            return None

    def save_excel(self, workbook, filename):
        try:
            workbook.save(filename)
        except Exception,e:
            print "Error:save exccel  failed!"
            return None
    def write_cell(self, sheet, row, col, value, style=None):
        try:
            borders = xlwt.Borders()
            borders.left = 1
            borders.right = 1
            borders.top = 1
            borders.bottom = 1

            self.style = xlwt.easyxf('align:wrap on, vert centre,horiz left')  # 自动换行，水平居中，垂直居左

            # 设置标题的格式，字体微软雅黑，加粗，背景色水绿色
            self.title = xlwt.easyxf(u'font:name 微软雅黑,height 240 ,colour_index black, bold on, italic off; align: wrap on, vert centre, horiz center;pattern: pattern solid, fore_colour aqua;')
        except Exception,e:
            print "Error!"

    def set_width(self, ws, col, width):
        try:
            ws.set_column(col, col, width)
        except Exception,e:
            print "Error!"

    def select_worksheet_by_name(self, name=u'Sheet1'):
        self.worksheet = self.workbook.sheet_by_name(name)

    def select_worksheet_by_index(self, index):
        self.worksheet = self.workbook.sheet_by_index(index)

    def get_row_values(self, index):
        if index < self.worksheet.nrows:
            return self.worksheet.row_values(index)
        else:
            return None

    def get_col_values(self, index):
        if index < self.worksheet.ncols:
            return self.worksheet.col_values(index)
        else:
            return None

    def get_value(self, row, col):
        try:
            return self.worksheet.row_values(row)[col]
        except Exception,e:
            return None

    def set_value(self, row, col, value):
        #put_cell(row, col, ctype, value, xf)
        # ctype:类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        # value = '单元格的值'
        #xf = 0 # 扩展的格式化
        try:
            return self.worksheet.put_cell(row, col, 1, value, 0)
        except Exception,e:
            return None