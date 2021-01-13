
'''增-append、删-pop、改、插insert、查'''

#列表【】，列表啥都可以放
lis = []
print(list)
print(type(list))
b = 6
a = [1,3,"4","a",b]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[0:2])
print(a[-1])

'''append,insert,extend'''
a.append(5)##末尾添加5
print(a)
a.pop(2)#2是索引。实际是删除了第3个
print(a)

a.insert(1,"b")#1是索引，在第二个位置插入b
print(a)

a[0] = "gai"#把第一个数改为“gai”，字符串不能改，如a='12345',a[0] = '67'报错
print(a)
c = "12345"
print(c[2])
#c[2] = 7
#print(c)


print(list('python'))