
lst = ["1","2","3",[1,2,3]]
lst.append(88)
print(lst)#['1', '2', '3', [1, 2, 3], 88]

lst.insert(3,[0,1])#在第4位插入一个列表
print(lst)#['1', '2', '3', [0, 1], [1, 2, 3], 88]

lst.extend([4,5,6])
print(lst)#['1', '2', '3', [0, 1], [1, 2, 3], 88, 4, 5, 6]
lst.remove('1')#移除某个具体的元素
print(lst)#['2', '3', [0, 1], [1, 2, 3], 88, 4, 5, 6]

lst.pop()
print(lst)#['2', '3', [0, 1], [1, 2, 3], 88, 4, 5]
lst.pop(2)
print(lst)#['2', '3', [1, 2, 3], 88, 4, 5]

lst.clear()#清空列表
print(lst)#[]

lst.extend([1,5,3,2,4,7])
print(lst)#[1, 5, 3, 2, 4, 7]
lst.sort()
print(lst)#[1, 2, 3, 4, 5, 7]

lst.reverse()
print(lst)#[7, 5, 4, 3, 2, 1]

print(sorted([3,5,2,6,9,7]))#[2, 3, 5, 6, 7, 9]
print(reversed([3,5,2,6,9,7]))
