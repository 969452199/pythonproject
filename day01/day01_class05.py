# #coding=utf-8
#
# #name = input("姓名")
# #print(name)
#1352368592
#1356169648
# #赋值相等
a = 12
print(id(a))
b = a
print(id(b))
c,d = 1,2
print(c)
print(d)




# # %取余；//取商；**取幂，pow(2,3)代表2的3次方；abs（）绝对值；round（）四舍五入；
#0,1,2,3,4,5,6,7,8,9,10,11,12,13,14(15个数，从0开始，不是1)
#-15，-14，-13，-12，-11，-10，-9，-8，-7，-6，-5，-4，-3，-2，-1
#s[开始索引:结束索引:步长]

print(s[])
a = 'you need python'
print(len(a))
print(a[0:3])
print(a[4:8])
print(a[9:])
print(a[::2])
print(a[::-2])
print(a[::-1])


#查看方法dir()
#查看文档help（）
a = "my"
b = "name"
c = "is xiaomin"
d = "DEER"
print(a+b+c)
print(a+' '+b+' '+c)
print(a,b,c)
print("y" in a)
print(a*4)
print(dir(str)) #查询字符串有哪些函数
print(help(str.format))
print(a.isdigit())#判断字符串是否由纯数字组成
print(a.upper())#字符串变大写
print(d.lower())#字符串变小写
f = ["lo","ve"]
print("*".join(f))#插入*,直接拼接所有字符串
print("*".join(b))
print(" ".join(b))
print("i love {}".format("python"))#拼接
print("i love {0} and {1}".format("python","we"))#带and拼接多个
print("i love {0} and {1} and {2}".format("python","jemeter","selenium"))
qw = " hello e"
print(qw.strip())#去左右空格
print(qw.replace(" ","*"))#*代替空格

