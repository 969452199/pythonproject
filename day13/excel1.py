import openpyxl
from openpyxl import load_workbook
from selenium import webdriver
import unittest,time,traceback,ddt
from ddt import unpack


#读取文件
class ParseExcel():
    def __init__(self,excelpath,sheetname):
        self.wd=load_workbook(excelpath)
        self.sheet=self.wd.get_sheet_by_name(sheetname)

    def getDataFromSheet(self):
        datalist = []
        for line in self.sheet.rows:
            tmplist = []
            tmplist.append(line[0].value)
            tmplist.append(line[1].value)
            datalist.append(tmplist)
        return datalist

# if __name__ == '__main__':
#     excelpath ='G:\\pythonproject\\new_table.xlsx'
#     sheetname = 'Sheet1'
#     pe = ParseExcel(excelpath,sheetname)
#     for i in pe.getDataFromSheet():
#         print(i[0])
#         print(i[1])

excelpath = 'G:\\pythonproject\\new_table.xlsx'
sheetname = 'Sheet1'
excel = ParseExcel(excelpath,sheetname)


@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUP(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*excel.getDataFromSheet())
    @unpack
    def test_databyfile(self,data,data1):
        print(data,data1)

if __name__=='__main__':
    unittest.main()