

#异常捕获，（try:、except:、else:、finally:）try执行正确，跳转else，不管对错，都会执行finally

while True:
    try:
        x = int(input('input a int number:'))
        r = 10/x
        print(r)
    except ZeroDivisionError:
        print('you should')
#   except BaseException as e:
#        print(e)
