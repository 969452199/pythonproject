class person:
    def __init__(self,name,age):
        self.name1 = name    #name1可随意命名
        self.age1 = age

    def get_name(self):
        return self.name1
    def get_age(self):
        return self.age1

class student(person):
    def __init__(self,school,name,age):
        self.school1 = school
        super().__init__(name,age)   #继承person函数中的name，age
        #person.__init__(self,name,age)
    def gread(self,n):
        print('{name} is {n} gread.'.format(name = self.name1,n = n))#打印出：..是几年级
        return self.school1   #返回学校名称

q = student(school='中心小学',name='小明',age='23')#直接传参数，定义了几个参数就可以传几个

print(q.gread(4))    #小明 is 4 gread.
                     #中心小学
# n要另外赋值,q.gread(4)把函数student(school='中心小学',name='小明',age='23')调用，输出print('{name} is {n} gread.'.format(name = self.name,n = n))


