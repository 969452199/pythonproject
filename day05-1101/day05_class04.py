f = open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8')
line = f.readline()
line = line[:-1]#去掉换行符

while line:
    print(line)
    line = f.readline()
    line = line[:-1]
f.close()


date2 = []
for line in open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8'):
    date2.append(line)
print(date2)
for i in date2:
    i.split('\n')
    print(i)
