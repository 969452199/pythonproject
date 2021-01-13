# 如果都是数字，则将该数字扩大10倍，然后打倒显示。
a = input('请输入：')
if a.isdigit():
    b = float(a) * 10
    print(b)
elif a.isalpha():
    b = a +'@python'
    print(b)
else:
    print(a)



# 如果是字母，则在其后面增加 ”@python“ 后打印显示。
# 其他情况则将输入的内容按原样显示

z = "Life is short You need python"
x = z.upper()
s = x.split()
print(s)

y = z.lower()
d = y.split()
print(d)
for word in d:
    len(word)
    print(word,'长度为',len(word))

le = [2,4,-7,19,-2,1.45]
for i in le:
    if i < 0:
        print(i)

la = {'python':89,'java':58,'physics':65,'math':49,'chinese':78}
sum = 0
for v in la:
    sum = sum +la[v]
print(sum)
lw = float(sum/len(la))
print(lw)
for i in la:
    if la[i] > lw:
        print(i)

a = range(1,100)
sum1 = 0
for t in a:
    sum1 = sum1 + t**2
print(sum1)










