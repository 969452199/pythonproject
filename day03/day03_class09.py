import random
a = random.randint(1,100)
print(a)
x = input('请输入数字：')
b = 1
while not x.isdigit():
    print('字符不对')
    x = input('请重新输入数字：')
    b += 1
if int(x) > a and b<= 3:
    print('数字过大哦')
    x = input('请重新输入数字：')
    b +=1
elif int(x) < a and b<= 3:
    print("数字太小")
    x = input('请重新输入数字：')
    b += 1
elif b >3:
    print('次数用完')
    b += 1
else:
    print('正确')
    b += 1



