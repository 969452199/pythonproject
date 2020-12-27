#圆括号内为元组，中括号为列表，只有一个元素的时候元素后需要加逗号

t = (1,3.12,[1,2,3],True,(5,6))
print(t)
print(type(t))
print(tuple())
print(bool(tuple()))
print(tuple('python'))
a = (3,)
print(a)
print(type(a))
b = (3)
print(b)
print(type(b))

print(t[2])
print(t[::2])

c = (9,4,0)
print(a + c)
print(c*2)
print(9 in c)
print(len(c))
#元组要修改时先转换成列表，再修改，再转换成元组
d = (23,54,56)
f = list(d)
print(d)
print(f)
f[0] = '34'
print(f)
