import xlrd
from xlutils.copy import copy

#打开文件
data = xlrd.open_workbook('G:\\pythonproject\\new_table.xls')
#查看工作表
data.sheet_names()
print("sheets:"+str(data.sheet_names()))


#读取某个表的行数和列数
#方法一：通过表名
table = data.sheet_by_name('Sheet2')
print("总行数："+str(table.nrows))
print("总列数："+str(table.ncols))
#方法二：通过索引获取表
table2 = data.sheet_by_index(1)
print("总行数："+str(table2.nrows))
print("总列数："+str(table2.ncols))

print("第一整行值："+str(table.row_values(0)))
print("第二整列值："+str(table.col_values(1)))

cel_B3 = table.cell(2,0).value
print("第三行第一列的值："+cel_B3)

#在Sheet3表中插入数据，第3行第二列
read_data = xlrd.open_workbook("G:\\pythonproject\\new_table.xls")
write_data = copy(read_data)
sheet_data = write_data.get_sheet("Sheet3")
sheet_data.write(2,1,'14')
write_data.save("G:\\pythonproject\\new_table.xls")