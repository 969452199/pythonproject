#coding=utf-8
a = 1
b = 2
c = a + b + True #True代表1
print(c)
print(type(c))
#print(type(str(c)))
print(str(c) + 'name')
d = 3
e = 4
f = d * e
print(f)
#变量的输入input
name = input("姓名")
print(name)
print(type(name))

#类型的转换 int();float()
g = 1 #整数转换
print(type(g))
print(type(float(a)))
print(type(str(g)))
h = 1.0  #浮点数转换
print(type(h))
print(type(int(h)))
print(type(str(h)))
i = '1234' #字符串转换
print(type(i))
print(type(int(i)))
print(type(str(i)))
print(type(float(i)))