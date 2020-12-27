'''def func(s):
    count = 0
    s:str
    if ii in s:
        count = count + 1
    return count
st = func('fsfrtgthy6')
print(st)'''

def classmate(name,sex = '男'):
    print('姓名:%s,性别:%s'%(name,sex))
classmate('张三')              #姓名:张三,性别:男
classmate(name='李四',sex='女')#姓名:李四,性别:女
classmate('王五','女')         #姓名:王五,性别:女
classmate(name='马六')        #姓名:马六,性别:男
#classmate(name='胡六','女')#会报错，先位置后关键字
classmate('胡六',sex='女')    #姓名:胡六,性别:女

def func(*args):
    print(args)
func(1)    #(1,)
func(2,3,4,'we',[1,5,4])   #返回元组(2, 3, 4, 'we', [1, 5, 4])

def func(*args,l =[]):  #2个参数，一个是动态参数，一个是默认参数，输出的结果也一定是2个数，一个是元组，一个是列表
    print(args,l)
func(2,3,4,'span',l=[2,3,4,5])  #元组加列表，除默认参数列表之外，前面输入的全纳入元组(2, 3, 4, 'span') [2, 3, 4, 5]

def func(name,sex,age,*args,key='key'):  #动态参数可以不传输，key = 'key'为默认参数
    print(name,sex,age)
    print(key)
    print(args)
func(2,3,4,'span',[1,2,3],'xiaoming')
#2 3 4
#key
#('span', [1, 2, 3], 'xiaoming')
func(4,5,6,)
#4 5 6
#key
#()

def sum(*args):
    res = 0
    for i in args:
        res +=i
    print(res)
res = sum(2,3,4)  #9

def sum(*args):
    res = 0
    for i in args:
        res +=i
    return res
res = [2,3,4]
print(sum(*res))#传入的是列表，得重新调用函数，不能忘记带*，相当于*args = *res ,9


def func(**kwargs):
    print(kwargs)
func(c =3,d=5)   #{'c': 3, 'd': 5}
dic = {'c':4,'d':6}
func(**dic)   #{'c': 4, 'd': 6}

a = 1
b = 7
c = 0
if a>b:
    c=a
else:
    c=b
print(c)  #7

