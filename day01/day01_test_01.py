# #coding=utf-8

'''三角形三条边长度分别为3、7、9，计算这个三角形的三角度数（用弧度制表示）
c^2=a^2+b^2-2abcosC'''
import math
a = 3
b = 7
c = 9
cosC = (a**2 + b**2 - c**2)/(2*a*b)
C = math.acos(cosC)
print(C)

cosA = (b**2 + c**2 - a**2)/(2*b*c)
A = math.acos(cosA)
print(A)

cosB = (a**2 + c**2 - b**2)/(2*a*c)
B = math.acos(cosB)
print(B)

'''对于字符串：‘you need python’'''
#– 分别得到三个单词
a = 'you need python'
print(len(a))
print(a[0:3])
print(a[4:8])
print(a[9:])
print(a.split())
#– 按照从左向右的顺序，隔一个字符取一个
print(a[::2])

#– 按照从右向左的顺序，隔一个字符取一个
print(a[::-2])

# 将字符串反序
print(a[::-1])

'''字符串 ’hello’， 字母 h 的左侧和 o 的右侧都有空格，使用字符串的方法去除空格'''
aa = " hello "
print(aa.strip())
print(aa[1:6])

#将字符串 ‘you need python’ 中的空格用 ”*“ 替代
bb = "you need python"
print(bb.replace(" ","*"))
print("*".join(bb.split()))






