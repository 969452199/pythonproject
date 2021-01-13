num1 = 0
num2 = 0

for p in range(1,100):
    if p %2 ==1:
        num1 = num1 + p
    else:
        num2 = num2 + p
print(num1-num2)