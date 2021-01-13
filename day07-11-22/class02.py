import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print('I was listening to %s.%s' %(func,ctime()))   #动态参数与时间参数（2个参数一起展示%s%s)
        sleep(1)              #等待1秒


def move(func):
    for i in range(2):
        print('I was at the %s! %s' %(func,ctime()))
        sleep(5)


def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print('error:The format is not recognise')


list = ['情人结.mp3','姜子牙.mp4']

threads = []
files = range(len(list))


for i in files:
    t = threading.Thread(target=player,args=[list[i]])
    threads.append(t)

if __name__=='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:%s'%ctime())

