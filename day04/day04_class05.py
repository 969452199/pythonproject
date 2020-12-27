
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

