lst1 = "python"
lst2 = "rust"
lst = list(lst1)
print(lst)
lst3 = list(lst2)
lst.extend(lst3)
#lst.extend(['r','u','s','t'])
print(lst)


lst.sort()
print(lst)

lst.remove('t')
print(lst)

lst.insert(4,'r')
print(lst)
lst.append(['e','w'])#append括号内的作为嵌入列表
print(lst)

c = ['19','12']
c.append(lst)
print(c)
