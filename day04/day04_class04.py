n = 1
def func():
    global n
    n +=1
func()
print(n)   #如果在局部内声明了,2

a = 1
b = 2
def func():
    x = 'aaa'
    y = 'bbb'
    print(locals())    #{'y': 'bbb', 'x': 'aaa'}
func()
print(globals())
#{'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000000248A240>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'G:/pythonproject/day04/day04_class04.py', '__cached__': None, 'n': 2, 'func': <function func at 0x0000000002939A60>,
# 'a': 1, 'b': 2}

import random
def func():
    sorce20 = []
    i = 0
    for i in range(1,21):
        sorce = random.randint(1, 101)
        i +=1
        sorce20.append(sorce)
    print(sorce20)
    return sorce20   #必须要有return，得出的结果才能被后面的函数调用
a =func()   #[67, 67, 18, 52, 46, 16, 65, 52, 19, 33, 31, 2, 100, 50, 26, 41, 93, 4, 46, 40]

def func(sorce20):
    dic={}
    for sorce2 in sorce20:
        if sorce2 > 90:
            dic[sorce2] ='优秀'
        elif sorce2 > 70:
            dic[sorce2] = '良好'
        elif sorce2 > 60:
            dic[sorce2] = '及格'
        else:
            dic[sorce2] = '不及格'
    print(dic)
func(a)   #传参，传上个函数的结果进入这个新函数中执行
#{67: '及格', 18: '不及格', 52: '不及格', 46: '不及格', 16: '不及格', 65: '及格', 19: '不及格', 33: '不及格', 31: '不及格', 2: '不及格', 100: '优秀', 50: '不及格', 26: '不及

import random
lit = [random.randint(0,100) for i in range(0,21)]
ditt = {}
def xy(a):
    def th():
        for i in lit:
            if i > 90:
                ditt[i] = '优秀'
            elif i > 80:
                ditt[i] = '良好'
            elif i > 60:
                ditt[i] = '及格'
            else:
                ditt[i] = '不及格'
        return ditt#最后结果
    return th
c = xy(lit)
d = c()
print(d)
#{14: '不及格', 25: '不及格', 39: '不及格', 82: '良好', 53: '不及格', 21: '不及格', 43: '不及格', 32: '不及格', 89: '良好', 38: '不及格', 79: '及格', 30: '不及格', 49: '不及