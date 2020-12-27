import math
def a(n):
    if n <=1:
        return False

def foo(x, y):
	print('x=', x)
	print('y=', y)
	return x+y
# 按位置调用：
foo(3, 4)
foo(4,3)
# 按名称调用：
foo(x=3, y=4)
foo(y=3, x=4)
# 设置默认值
def bar(x, y=4):
	print('x=', x)
	print('y=', y)
	return x+y
print(bar(6))
print(bar(2, 6))
print(bar(x=3, y=9))
print(bar(y=8, x=5))

def sum1(*args):
    sum2 = 0
    for i in args:
        sum2 += i
        return sum2
print(args(2,3))
