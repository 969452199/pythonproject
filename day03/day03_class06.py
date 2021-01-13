#1、字典键值对位置互换，直接d[value]=key；
#2、 如果value为列表时，需要转换成元组，用if判断，if type(value) == list  value = tuple(value),然后输出字典


d = {'book':['python', 'datascience'],'author':'laoqu','publisher':'phei'}
a = d.items()
print(a)
e = { }
for x,y in d.items():
    if type(y) == list:
        y = tuple(y)
        e[y] = x
    else:
        e[y] = x
print(e)




