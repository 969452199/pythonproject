def bar(x):
    def par(y):
        C = x/y
        return C
    return par

a = bar(3)   # x=3,bar(3)=par=a, 则 par(9)=a(9), 那么 y=9
b = a(9)     #a就是par
print(b)    # 3/9=0.3333333333333333

