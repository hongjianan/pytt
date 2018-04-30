# -*- coding: utf-8 -*-

import xlsxwriter


class Excel():
    '''
    '''

    def __init__(self, filename):
        self.filename = filename
        self.book = xlsxwriter.Workbook(filename)
        self.sheet = {}

    def close(self):
        self.book.close()

    # def read(self):
    #     pass

    def write(self, sheet, pos_x, pox_y, text, fmt = None):
        if fmt:
            return sheet.write(pos_x, pox_y, text, fmt)
        return sheet.write(pos_x, pox_y, text)

    def add_sheet(self, sheet_name):
        sheet = self.book.add_worksheet()
        self.sheet[sheet_name] = sheet
        return sheet

    def get_sheet(self, sheet_name):
        return self.sheet[sheet_name]

'''
class ExcelReader(Excel):
    def __init__(self, filename):
        Excel.__init__(self, filename)

    def read(self):
        return Excel.read(self)

class ExcelWriter(Excel):
    def __init__(self, filename):
        Excel.__init__(self, filename);

    def

    def write(self):
        return Excel.write(self)
'''


def run():
    print("start create xlsx")
    excel = Excel("test.xlsx")
    sheet1 = excel.add_sheet(1)
    excel.write(sheet1, 0, 0, "name")
    excel.write(sheet1, 0, 1, "sex")
    excel.write(sheet1, 0, 2, "age")
    excel.close()
    print("create xlsx success")

if __name__ == "__main__":
    run()
