a = {'usa':'newyork','china':'beijing','japan':'tokeyo'}
print(a)
print(a.get('usa'))
print(a.setdefault('china'))
print(a.get('japan'))

b = input("请输入国家名字：")
print(b)
a = {'usa':'newyork','china':'beijing','japan':'tokeyo'}
print(a.get(b))
