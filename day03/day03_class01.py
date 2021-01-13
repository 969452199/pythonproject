a = 'hello'
for i in a:
    print(i)

lst = [1,2,3,4]
for i in lst:
    print(i)

t = tuple(lst)
for i in t:
    print(i)

b = {'name':'xiaoming','age':'10','sex':'men'}
for i in b:
    print(i)
    print(b[i])
    print(i,b[i])

#有问题
m = {'name':'xiaoming','age':'10','sex':{'men':{'a':1}}}
print(m['sex']['men']['a'])
for k,n in m.items():
    print(k,n)


dic = {'a':12,'b':13,'c':14}
# for a,m in dic.items():
#     print(a,m)
print(dic.items())
