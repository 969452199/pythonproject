lst = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
list3 =[]
for ii in lst:
    #for i2 in lst2:
        # print(i2)1
        # print(ii.endswith(i2))
    if  ii.endswith('.jpg'):
        list3.append(ii)
    elif ii.endswith('.gif'):
        list3.append(ii)
    elif ii.endswith('.png'):
        list3.append(ii)
print(list3)

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = zip(a,b)
print(list(c))
print(dict(zip(a,b)))