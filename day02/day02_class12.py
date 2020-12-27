
a = input('请输入数字：')
while not a.isdigit():
    print('输入内容非数字')
    a = (input('请重新输入数字：'))
a = int(a)
if a % 2 == 0:
    print(str(a), '为偶数')
else:
    print(str(a), '为奇数')


b = input('请输入域名：')
if b.startswith('www.') and len(b.split('.')) >=3:
    print('域名正确')
else:
    print('域名格式不正确')
