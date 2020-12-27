import threading
from time import ctime,sleep
# def music(func):
#     for i in range(2):
#         print('I was listening to %s.%s' %(func,ctime()))   #动态参数与时间参数（2个参数一起展示%s%s)
#         sleep(1)              #等待1秒
#
#
# def move(func):
#     for i in range(2):
#         print('I was at the %s! %s' %(func,ctime()))
#         sleep(5)

def super_player(file,time):
    for i in range(3):
        print('Start playing： %s! %s' %(file,ctime()))
        sleep(time)

list = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}
files = range(len(list))

threads = []
for file,time in list.items():   #得出每个键值对的具体数值
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__=='__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:%s'%ctime())
