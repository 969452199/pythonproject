#coding=utf-8
#嵌套多个列表切片
lit = [1,2,"a",["1","2","3",["12","23"]]]
print(lit)
print(lit[3])
print(lit[3][3])
print(lit[3][3][0])#取“12”

#赋值切片
lit1 = lit[3]
print(lit1)
lit2 = lit1[3]
print(lit2)
lit3 = lit2[0]
print(lit3)
#取2/5/9
lis = [[1,2,3],[4,5,6],[7,8,9]]
print(lis[0][1])
print(lis[1][1])
print(lis[2][2])

lis1 = lis[0]
print(lis1[1])
lis2 = lis[1]
print(lis2[1])
lis3 = lis[2]
print(lis3[2])

print(lis[-3][-2])
print(lis[-2][-2])
print(lis[-1][-1])

lie = [1,2,3]
lie1 = [4,5,6]
print(lie + lie1)#2个列表拼接,有前后顺序
lie.extend(lie1)#lie与lie1位置可互换，得出不同序列的列表
print(lie)
print(lie*2)#列表重复
lie2 = lie1*4
print(len(lie2))
print(5 in lie2)
print(lie2)
lie[2] = 0
print(lie)

#lie3 = lie.extend(lie1)
#print(lie3)

#d = [3,4,5,6]
#print(d)
#print(d.remove(3))