def my_len():
    '''计算ls的长度,my_len为函数名字'''
    ls = input('please input:')
    length = 0
    for i in ls:
        length = length + 1
    print(length)
    return length#要有return才有返回
a = my_len()
print(a)
#返回多个变量要多个接收，返回多个变量用逗号隔开，一个接收就是元组形式
#先位置，后关键字
