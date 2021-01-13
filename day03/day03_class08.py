#随机数
import random
a = random.randint(1,100)
print(a)
x = int(input('请输入数字：'))
b = 1
while x != a:
    if x > a and b <=3:
        print('数字过大哦')
        x = int(input('请重新输入数字：'))
        b +=1
    elif x < a and b <=3:
        print("数字太小")
        x = int(input('请重新输入数字：'))
        b += 1
    else:
        print('次数用完')
        break
else:
    print('正确')
