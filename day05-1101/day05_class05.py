with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    f.write('hello,world!')
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())

with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    f.writelines('hello,world!\nmy name is xu')#换行
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())


