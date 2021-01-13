a = 3
while a >0:
    if a %2 ==0:
        break
    else:
        print(a)
    a -=1

b = 2
while b >0:
    b -= 1
    print(b)
#continue跳过后面的同条件
x = 10
while x > 0:
    x -=1
    if x == 5:
 #       print(x)
        continue
        print(x)
    else:
        print(x)

c = 100
while c %2 ==0:
    c -=1
    if c//2 <=10:
        continue
        print(c)
    else:
        print(c)

c = 0
while c<1:
    c +=1
    print(c)
    break
else:
    print('break')

for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print(n,'=',x,'*',n/x)
            break
    else:
        print(n,'is a prime number')