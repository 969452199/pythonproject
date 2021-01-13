a = (1,2,3,4)
b = (5,6,7,8)
c = zip(a,b)
print(c)
print(list(c))#[(1, 5), (2, 6), (3, 7), (4, 8)]
d = dict(zip(a,b))
print(d)#{1: 5, 2: 6, 3: 7, 4: 8}
e = enumerate(a)
print(dict(e))#{0: 1, 1: 2, 2: 3, 3: 4}

m = range(2,22,2)
for i in m:
    print(i)


lst = []
for x,y in zip(a,b):
    lst.append(x+y)
print(lst)#[6, 8, 10, 12]

w = [x + y for x,y in zip(a,b)]
print(w)#[6, 8, 10, 12]

#e与lt结果一致
e = [i for i in range(1,20) if i%2 ==0 ]
print(e)#[2, 4, 6, 8, 10, 12, 14, 16, 18]

lt = []
for i in range(1,20):
    if i %2 ==0:
        lt.append(i)
print(lt)#[2, 4, 6, 8, 10, 12, 14, 16, 18]

