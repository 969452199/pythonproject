#excel操作
import xlrd
from xlutils.copy import copy
class excel_e():
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'D:/py/excel.xls'
        else:
            self.file_path = file_path
        self.data = xlrd.open_workbook(self.file_path)

    def read_cell(self,sheet,column,line):
        try:
            table = self.data.sheet_by_name(sheet)
            cell = table.cell(column,line).value
            return cell
        except BaseException as e1:
            return e1

    def column_all(self,sheet):
        try:
            table = self.data.sheet_by_name(sheet)
            column = table.nrows
            if column == 1:
                al1 = table.row_values(column - 1)
            else :
                al1 = []
                for i in range(column):
                    al1.append(table.row_values(i))
            return al1
        except BaseException as e2:
            return e2

    def line_all(self,sheet):
        try:
            table = self.data.sheet_by_name(sheet)
            line = table.ncols
            if line == 1:
                al1 = table.col_values(line - 1)
            else :
                al1 = []
                for i in range(line):
                    al1.append(table.col_values(i))
            return al1
        except BaseException as e3:
            return e3

    def write(self,Sheet,column,line,value):
        try:
            write_data = copy(self.data)
            sheet_data = write_data.get_sheet(Sheet)
            sheet_data.write(column, line, value)
            write_data.save(self.file_path)
        except BaseException as e4:
            return e4

if __name__ == "__main__":
    c = excel_e("D\\")
