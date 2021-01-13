#传参，函数定义时要有形参path
def func(path,encoding='utf-8'):
    try:
        q = open(path,'r', encoding='utf-8')
        d = q.read()
        q.close()
    except BaseException as e:
        print(e)
    else:
        return d
con = func('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt',encoding='utf-8')
print(con)