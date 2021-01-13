a = 1

for a in range (1,10):
    for b in range (1,1+a):
        print('%d * %d = %d\t' %(b,a,a*b))

for c in range (1,10):
    for d in range (1,1+c):
        lt = c*d
        print(c,'*',d,'=',lt)


