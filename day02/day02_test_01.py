
#移除 name 变量对应的值两边的空格，并输入移除后的内容
name = " aleX "
name1 = name.strip()
#print(name1)
print('移除空格 \n'+name1)


# 判断 name 变量对应的值是否以 "al" 开头，并输出结果
test = name1
print('是否以al开头？')
print(test.startswith('al'))

# if name.startswith(' al'):
#     print('name start with',' al')
#     print(bool(name))
# else:
#     print(bool(name))

# c. 判断 name 变量对应的值是否以 "X" 结尾，并输出结果
print('是否以X结尾？')
print(test.endswith('X'))
# d. 将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果
print('将 name 变量对应的值中的 “l” 替换为 “p”')
print(test.replace('l','p'))
# e. 将 name 变量对应的值根据 “l” 分割，并输出结果。
print('将 name 变量对应的值根据 “l” 分割')
new = test.split('l')
print(new)
# f. 请问，上一题分割之后得到值是什么类型（可选）？
print(type(new))
# g. 将 name 变量对应的值变大写，并输出结果
print('名字大写： \n' +test.upper() )
# h. 将 name 变量对应的值变小写，并输出结果
print('名字小写： \n' +test.lower())
# i. 请输出 name 变量对应的值的第 2 个字符？
print('输出'+test+'第二个字符: \n' +test[1])
# j. 请输出 name 变量对应的值的前 3 个字符？
print('输出'+test+'前三个字符: \n' +test[0:3])
# k. 请输出 name 变量对应的值的后 2 个字符？
#print(test[-1:-3:-1])
print('输出'+test+'最后两个字符: \n' +test[2:])
print('输出'+test+'最后两个字符:\n' + test[len(test)-2:len(test)])


str1 = "猿说python"
print(len(str1))            # 内置函数 len() 获取字符串长度
print(str1)                 # 打印字符串
print(str1[2])              # 获取字符串中的第二个字符
print(str1[0:2])            # 截取字符串索引值为0~1的字符，不包括索引值为2的字符
print(str1[2:5])            # 截取字符串索引值为2~4的字符，不包括索引值为5的字符
print(str1[2:-1])           # 截取字符串重索引值为2开始直到字符串结尾的前一个，-1的索引值表示最后一个
print(str1[2:len(str1)])    # 截取字符串索引值2~8，最后一个字符的索引值为7，所以刚刚好能截取到字符串末尾