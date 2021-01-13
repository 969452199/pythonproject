#coding=utf-8
# 1.创建一个空的列表score
sorce = []
print(sorce)

# 2.往创建的列表添加10个元素（自己自定义元素）
sorce.extend([43,76,88,89,100,59,49,100,89])
print(sorce)  #[43, 76, 88, 89, 100, 59, 49, 100, 89]

# 3.输出score列表中第3个元素的数值
print(sorce[2])  #88

# 4.输出score列表中第1-6个元素的值
print(sorce[0:6])  #[43, 76, 88, 89, 100, 59]

# 5.利用insert函数，在score列表中的第3个元素之前添加数值59
sorce.insert(2,59)
print(sorce)   #[43, 76, 59, 88, 89, 100, 59, 49, 100, 89]

# 6.利用变量num保存数值76，调用count函数，查询变量num变量值在score列表中出现的次数
num = 76
print(sorce.count(num))  #1

# 7.使用in查询score列表中是否有num变量的考试成绩
print(num in sorce)  #True

# 8.调用index函数，查询score列表中成绩是满分的学生学号
print(sorce.index(100))   #5

# 9.在score列表中，将59分加1分
for i in range(len(sorce)):
    r = sorce[i] 
    if(r==59):
        r = r + 1
        sorce[i] =r
print(sorce)   #[43, 76, 60, 88, 89, 100, 60, 49, 100, 89]


# for r in sorce:
#     if r == 59:
#         r = r + 1
#         print(r)
# print(sorce)

# 10.调用del函数，删除列表中第一个元素
sorce.pop(0)
print(sorce)   #[76, 60, 88, 89, 100, 60, 49, 100, 89]

# 11.调用len函数获得score列表中元素的个数
print(len(sorce))  #9

# 12.调用sort函数，对列表中的元素进行排序
sorce.sort()
print(sorce)  #[49, 60, 60, 76, 88, 89, 89, 100, 100]

# 13.调用reverse函数，颠倒score列表中的顺序
sorce.reverse()
print(sorce)   #[100, 100, 89, 89, 88, 76, 60, 60, 49]

# 14.调用pop函数，删除score列表中尾部的元素，返回删除了的元素
print(sorce.pop())  #49

# 15.score列表中，追加数值88，并输出。调用remove函数，删除score列表中的第一个88
sorce.append(88)
print(sorce)   #[100, 100, 89, 89, 88, 76, 60, 60, 88]
sorce.remove(88)
print(sorce)   #[100, 100, 89, 89, 76, 60, 60, 88]

# 16.创建2个列表score1和score2，score1中包含2个元素值：80，61 ，score2中包含3个元素值，71,95,82，合并这2个列表，并输出全部元素
sorce1 = [80,61]
sorce2 = [71,95,82]
sorce1.extend(sorce2)
print(sorce1)   #[80, 61, 71, 95, 82]

# 17.创建score1列表，其中包含2个数值：80,61，将score1 中的元素复制5次后保存在score2列表中，输出score2列表中的全部元素。
sorce3 = [80,61]
sorce2.extend(sorce3*5)
print(sorce2)   #[71, 95, 82, 80, 61, 80, 61, 80, 61, 80, 61, 80, 61]

# 18.写出判断一个数是否能同时被3和7整除的条件语句，并且打印对应结果。
lst =input("1请输入数字：")
lst = int(lst)
if lst % 21 == 0:
    print(str(lst),'可以同时整除')
else:
    print(str(lst),'不可以同时整除')

# 19.写出判断一个数是否能被3或7整除，但是不能同时被3和7整除的条件语句，并打印相应的结果
lsw = input("2请输入数字：")
lsw = int(lsw)
if (lsw %3 ==0 or lsw %7 ==0) and lsw %21 !=0:
    print(str(lsw), '符合要求')
else:
    print(str(lsw), '不符合要求')

# 20.输入年，写代码判断输入的年是否是闰年，并打印对应的结果。（余年的条件是：能够被4整除但是不能被100整除或者能够被400整除）
lsq = input("请输入年份：")
lsq = int(lsq)
if (lsq %4 ==0 and lsq %100 !=0 )or lsq %400 ==0:
    print(str(lsq),'是闰年')
else:
    print(str(lsq),'不是闰年')

# 21.假设今天的上课时间是34527秒，请用编程计算今天上课时间是多少小时，多少分钟，多少秒；以'xx时xx分钟xx秒'的方式表示出来。
a = 34527
b = a //3600
c = (a % 3600)//60
d = (a % 3600) % 60
print('今天上课时长为：',b,'时',c,'分',d,'秒')  #今天上课时长为： 9 时 35 分 27 秒

# 22.定义两个变量保存一个人的身高体重，编程实现这个人的身材是否正常！公式：体重（kg）/身高（m）的平方值在18.5~24.9之间属于正常
high = input('请输入身高(m)：')
weight = input('请输入体重(kg)：')
qw = float(high)
qe = float(weight)
if 18.5 < qe / qw**2 <24.9:
    print("体重正常")
elif qe / qw**2<18.5:
    print("体重偏轻，请增强营养")
else:
    print('有点超重哦，请控制饮食')
