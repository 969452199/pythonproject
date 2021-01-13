# 1、写函数，计算传入字符串中的【数字】、【字母】、【空格】和【其他】的个数
a = '12 n he ui$345%46@'
b = list(a)
print(b)   #['1', '2', ' ', 'n', ' ', 'h', 'e', ' ', 'u', 'i', '$', '3', '4', '5', '%', '4', '6', '@']
word: int = 0
digs: int = 0
spac: int = 0
othe: int = 0
for i in range(len(b)):
    r:str = b[i]
    if r.isdigit():
        digs +=1
    elif r.isalpha():
        word +=1
    elif r.isspace():
        spac +=1
    else:
        othe +=1
print('数字：',digs,'，字母：',word,'，空格：',spac,'，其它：',othe) #数字： 7 ，字母： 5 ，空格： 3 ，其它： 3




# 2、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5

def fun1(argv):
    if len(argv) > 5:
        return True
    else:
        return False
a = input('请输入内容：')  #sdgfdh
print(fun1(a))          #True


# 3、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def list1(n1):
    n2 = []
    for i in range(len(n1)):
        if i <= 1:
            n2.append(n1[i])
        else:
            pass
    return n2
ae = [23,45,345,876,354]
p = list1(ae)
print(ae)   #[23, 45, 345, 876, 354]
print(p)    #[23, 45]



# 4、输出1,2,3,4,5,6,8,9,10
num1 = 0
num2 = []
while num1 <10:
    num1 +=1
    if num1 !=7:
        num2.append(num1)
        #print(num1)
    # else:
        #num2.append(num1)
print(num2)   #[1, 2, 3, 4, 5, 6, 8, 9, 10]

# 5、输出1-2+3-4+5.....99所有数的和
num1 = 0
num2 = 0
for p in range(1,100):
    if p %2 ==1:
        num1 = num1 + p
    else:
        num2 = num2 + p
print(num1-num2)    #50


# 6、有字符串'python'，使用适当的语句，将此字符串中每个字符与一个变量建立引用关系，即依次通过若干个变量，可以得到此字符串中的每个字符。
a,b,c,d,e,f='python'
print(a)   #p
print(b)   #y
print(c)   #t
print(d)   #h
print(e)   #o
print(f)   #n


# 7、在某个歌唱比赛中，评委们对每个参赛歌手进行打分，通常计算歌手最终得分的方法是去掉最高分，去掉最低分，然后将剩下的分数计算平均分，
# 此平均分即为歌手最终得分。假设评委们对某歌手的评分是(10分满分）：[9.9, 9.2, 8.1, 9.7, 10, 8.3, 8.6, 9.5, 8.4]，
# 请按照上述方法，计算歌手的最终得分（保留一位小数）
sorce = [9.9, 9.2, 8.1, 9.7, 10, 8.3, 8.6, 9.5, 8.4]
sorce.sort()
sorce_new = sorce[1:-1]    #去头去尾
print(sorce_new)           #[8.3, 8.4, 8.6, 9.2, 9.5, 9.7, 9.9]
sorce1 = sum(sorce_new)/len(sorce_new)
sorce1 = round(sorce1,1)
print(sorce1)    #9.1


# 8、d = {'huawei': 91.2, 'alibaba': 94.1, 'qq':90.1, 'baidu':89.4, 'xiaomi':88.4}，找出其中键值对的值最小的那个键值对。
d = {'huawei': 91.2, 'alibaba': 94.1, 'qq':90.1, 'baidu':89.4, 'xiaomi':88.4}
e = []
for s in d:
    r = d[s]
    e.append(r)
print(e)    #[91.2, 94.1, 90.1, 89.4, 88.4]
e.sort()
f = e[0]
print(f)   #88.4
if r == f:
    #print(s,f)      #xiaomi 88.4
    print(s,d[s])    #xiaomi 88.4


# 9、 假设列表中有多个文件名，['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']，
# 编写程序，从这些文件中选出图片文件，即扩展名分别是('.jpg', '.gif', '.png')的文件。
lst = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
lst2 = ['.jpg','.gif','.png']
list3 =[]
for ii in lst:
    i2: str
    for i2 in lst2:
        # print(i2)1
        # print(ii.endswith(i2))
        if  ii.endswith(i2):
            list3.append(ii)
print(list3)     #['b.jpg', 'c.gif', 'e.png', 'f.jpg', 'f.gif', 'h.png']
    # print(ii.split('.jpg'))
    # if ii.split('.jpg'):
    #     lst2.append(ii)
    #     print(lst2)

# 10、 有列表[1, "a", 2, "b", 3, "c", 4, "d"]，要求交替使用列表中的元素作为字典的键和值，创建一个字典，即得到字典{1: "a", 2: "b", 3: "c", 4: "d"}。
lsst =[1, "a", 2, "b", 3, "c", 4, "d"]
lss1 = []
lss2 = []
for zx in range(len(lsst)):
    if zx %2 ==1:
        lss1.append(lsst[zx])
    else:
        lss2.append(lsst[zx])
print(lss2)         #[1, 2, 3, 4]
print(lss1)         #['a', 'b', 'c', 'd']
lss3 = zip(lss2,lss1)
print(lss3)         #<zip object at 0x0000000002563648>
print(list(lss3))   #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
d = dict(zip(lss2,lss1))
print(d)            #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}




