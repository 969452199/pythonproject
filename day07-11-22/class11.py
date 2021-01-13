a = {'we':3,'c':4}
b = {'d':5}
a1 = a.items()
print(a1)
b1 = b.items()
print(b1)
c = dict(a,**b)
print(c)    #两个字典相加，第二个加数前面必须加**，用dict函数
