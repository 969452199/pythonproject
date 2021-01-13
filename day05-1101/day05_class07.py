da1 = [['a','b','c'],['1','2','3'],['a','b','c']]
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    f.write(da1)
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())
'''    for i in da1:
        i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'
        f.write(i)'''