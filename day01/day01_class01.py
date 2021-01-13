#coding=utf-8
#注释作用，print(type(a))查看a的类型,True/Forth为布尔值，首字母必须大写,1/0
#数字型：整型、浮点数，布尔值，复数；非数字型：字符串，元祖-带括号，例如（1,2,3,4）tuple；列表是中括号【】list，括号内可放任何东西，
# 可以是字符串、数字、元祖；
#字典：name={“”},dict
a = 'hello,'
b = 'world!'
c1 = a + b
print(c1)
print(type(c1))
c = 3
d = 4
e = c + d
print(e)
print(type(e))
#字典：
name = {'key':'2','key1':'3'}
name2 = {1,2,3,4} #集合set

#格式化--占位符：字符串,保留3位小数--%。03f

name2 = "xiaoming"
age = 78.1234
print("my name is %s %d %.03f" %(name2,age,age))
print( "my name is "+ name2+"78")