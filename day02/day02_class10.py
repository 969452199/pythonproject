
import  copy

a = set([1,2,3,4,5,6])
b = set([2,5,7])
print(a.issuperset(b))#a包含b
print(b.issubset(a))#b是a的子集

print(a | b)#并集
print(a & b)#交集
print(a - b)#差集
print(b - a)
c = copy.copy(a)
print(c)
a.add(7)
print(a)
print(c)

aa = [1,2,3,4,['a','b']]
bb = aa
cc = copy.copy(aa)#浅拷贝会拷贝小容器变化的数值
dd = copy.deepcopy(aa)#深拷贝保持原始数值
aa.append(5)
aa[4].append('c')
print('aa=',aa)
print('bb=',bb)
print('cc=',cc)
print('dd=',dd)


skills = {'Python','R','SQL','Git','Tableau','SAS'}
myskills = {'Python','R'}
print(myskills.issubset(skills))
print(skills & myskills)
a1 = (skills & myskills)
print(a1)
print(bool(a1))

#如果 bool(expr) == Flase


print(1 and 2)
print(0 and 2)
print(3<4 and 4>5)

print(1 or 2)
print(0 or 2)
print(3<4 or 4>5)

print(not (1))
print(not(0))