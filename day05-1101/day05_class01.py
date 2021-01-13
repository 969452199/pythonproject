#coding=utf-8
#路径要么是双斜杠，要么是单反斜杠
#在本目录下可以相对路径，否则要绝对路径
f = open("G:\\1-2020川石自动化\\第五节课-11-01\\date.txt",'r',encoding='utf-8')
c = f.read()
print(c)
r = f.readline()
print(r)
f.close()
#readline

'''path = input('输入路径：')
meth = input('输入读取方式：')
def func():
    try:
        q = open(path, meth, encoding='utf-8')
        d = q.read()
        print(d)
        q.close()
    except BaseException as e:
        print(e)
func()'''
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    str  = f.read()
    print(str)






