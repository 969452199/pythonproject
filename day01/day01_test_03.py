
## coding=utf-8


'''数学运算一定要转换成数字型，如int、float等'''
#– 询问用户姓名和年龄
#– 计算10年之后的年龄
#– 打印出用户的姓名，及其现在和10年之后的年龄

name = input("What's your name?")
age = input("How old are you?")
while not age.isdigit():
    print("The age should be integer number!")
    age = input("How old are you?")
age_10 = int(age) + 10
print(name)
print(age_10)
print("Nice to be meet you,{0}".format(name))
print("you are {0} years old, and 10 years later you are {1} years old !".format(age,age_10))
