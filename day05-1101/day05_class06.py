'''da = ['a','b','c']
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    f.writelines(da)
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())

#replace('\'','')表示去单引号
da1 = [['a','b','c'],['1','2','3'],['a','b','c']]
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    for i in da1:
        i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'
        f.write(i)

with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())

da2 = [['a','b','c'],['1','2','3'],['a','b','c']]
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','w',encoding='utf-8') as f:
    for r in da2:
        f.writelines(r)
with open('G:\\1-2020川石自动化\\第五节课-11-01\\date.txt','r',encoding='utf-8') as f:
    print(f.read())'''



class data:

    def __init__(self,file_path = None):
        if file_path == None:
            self.file_path = "G:\\1-2020川石自动化\\第五节课-11-01\\date.txt"
        else:
            self.file_path = file_path
    def read_txt(self):
        with open(self.file_path,'r',encoding='utf-8') as f:
            neir = f.read()
            return neir
    def write_txt(self,ner1):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(ner1)
if __name__=='__main'
    s = data()
    ner1 = '3435dfg'
    print(s.write_txt(ner1))



