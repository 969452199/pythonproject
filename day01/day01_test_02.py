#通过键盘输入数字，作为圆的半径
#– 计算圆的周长和面积，并分别打印显示出来，结果保留两位小数
import math
r = input("请输入圆的半径：")
if not r.isdigit():#判断字符串是否由纯数字组成
    print("请输入数字！")
    exit()
r = float(r)
C = 2*math.pi*r
S = math.pi*(r**2)
print("圆的周长为： %.02f" %C)
print("圆的面积为： %.02f" %S)



import math
r = input("请输入圆的半径：")
while not r.isdigit():
    print("请输入数字！")
    r = input("请重新输入圆的半径：")
r = float(r)#浮点数转换
c = 2*math.pi*r
s = math.pi*r**2
print("圆的周长为：", round(c, 2))
print("圆的面积为：", round(s, 2))