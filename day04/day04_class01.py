#coding=utf-8

def my_len():
    '''计算ls的长度'''
    ls = 'hello world'
    length = 0
    for i in ls:
        length = length + 1
    print(length)         #11
    return  length
str_len = my_len()#函数调用
print('str_len:%s'%str_len)    #变动参数引用 str_len:11
print('str_len:{}'.format(str_len))  #str_len:11

def name():
    name = input('please input your name:')   #dg
    return name
my_name = name()
print(my_name)      #dg

#返回多个变量要多个接收，返回多个变量用逗号隔开，一个接收就是元组形式
#先位置，后关键字
def func():
    return 'a','b','c'
d,e,f = func()
print(d,e,f)   #a b c
qw = func()
print(qw)      #('a', 'b', 'c')元组形式

def func():
    return [1,2,3]
a,b,c = func()
print(a,b,c)     #1 2 3
qe = func()
print(qe)        #[1, 2, 3]

def func():
    return {'name':'span','age':13}
#dice,dicr = func()
#print(dice,dicr)   #多个值接收,只返回键不返回值
dic = func()
print(dic)  #{'name': 'span', 'age': 13}字典不能通过多个值接收，只能一个接收




