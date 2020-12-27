
'''集合'''
l1 = set([1,2])#{1, 2}
print(l1)
l2 = {1,(1,2,3)}
print(l2)#{1, (1, 2, 3)}

l3 = {2,3,4,2,3,5}#集合互异
print(l3)#{2, 3, 4, 5}
print(type(l3))#<class 'set'>
l4 = {3,2,4,5}
print(l3 == l4)#无序性#True
print([1,2,3] == [2,1,3])#False

#列表不能作为集合的元素
#a = {1,2,[3,4]}
#创建可变集合用set()，不可变用frozonset()
a = [1,2,3,4,5,5,6]
print(a)#[1, 2, 3, 4, 5, 5, 6]
b = set(a)
print(b)#{1, 2, 3, 4, 5, 6}

b.add(7)
print(b)#{1, 2, 3, 4, 5, 6, 7}
b.update(set([8,'hello']))#增加需要集合形式，故需要加set
print(b)#{1, 2, 3, 4, 5, 6, 7, 8, 'hello'}

b.pop()#删除，从前面开始删除
print(b)#{2, 3, 4, 5, 6, 7, 8, 'hello'}
b.pop()
print(b)#{3, 4, 5, 6, 7, 8, 'hello'}

b.remove(8)#删除，指定删除,当不存在时报错
print(b)#{3, 4, 5, 6, 7, 'hello'}
#b.remove(8)
#print(b)

b.discard(4)#删除，指定删除,当不存在时不报错
print(b)#{3, 5, 6, 7, 'hello'}
b.discard(8)
print(b)#{3, 5, 6, 7, 'hello'}
#b.clear()
#print(b)
print(5 in b)#判断元素是否在集合中用in
print(8 in b)

#lst = set(1,2,[1,2])
#print(lst)
#lst = set(1,2,(2,3))
#print(lst)