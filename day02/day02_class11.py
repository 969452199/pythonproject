
'''if语句'''
#当输入要素为整型时，调用input，输出的是字符串，所以需要int转换
x = int(input('请输入成绩：'))
if x >= 90:
    print('优秀')
elif x >= 70:
    print('良好')
elif x >= 60:
    print('及格')
else:
    print('继续加油')

#a = int(input('请输入数字：'))
#b = 'python' if a > 3 else 'rust'
#print(b)

a = int(input('请输入数字：'))
if a % 2 == 0:
    print(str(a),'为偶数')
else:
    print(str(a),'为奇数')
