
class mytest: #mytest为类的名称，可随意命名
    def __init__(self,name): #init初始化，参数name可填可不填
        self.name1 = name
        self.kongfu = 'xianglongshibazhang' #初始化后面不能带return
    def done(self): #方法，行为命名可随意命名
        self.sex = 'wormen'
        return 'coding'

p = mytest('chenglong') #实例化
print(p.name1)                # chenglong
print(p.done())               # coding
print(p.kongfu)               # xianglongshibazhang
print(p.sex)                  # wormen
print(mytest('wanger').name1) # wanger  mytest('wanger').name1等价于p.name1



class animal(object):
    def __init__(self,name):
        self.name = name
    def moth(self):
        print(self.name+'的嘴巴制作完成')
    def ear(self):
        print(self.name+'的耳朵制作完成')
    def eye(self):
        print(self.name+'的眼睛制作完成')
    def head(self):
        print(self.name+'的头部制作完成')
    def body(self):
        print(self.name+'的身体制作完成')
    def foot(self):
        print(self.name+'的脚制作完成')
    def makeall(self):
        self.moth()
        self.ear()
        self.eye()
        self.head()
        self.body()
        self.foot()
        return self.name
q = animal('猪')
print(q.makeall())
# 猪的嘴巴制作完成
# 猪的耳朵制作完成
# 猪的眼睛制作完成
# 猪的头部制作完成
# 猪的身体制作完成
# 猪的脚制作完成
# 猪



#class可以继承
class pig(animal):
    def wing(self):
        print(self.name+'的翅膀制作完成')
qi = pig('小鸡')
qi.makeall()       #小鸡的嘴巴制作完成
                   #小鸡的嘴巴制作完成
                   # 小鸡的耳朵制作完成
                   # 小鸡的眼睛制作完成
                   # 小鸡的头部制作完成
                   # 小鸡的身体制作完成
                   # 小鸡的脚制作完成
qi.wing()  #鸡的翅膀制作完成