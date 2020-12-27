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

threads = []
t1 = threading.Thread(target=music,args=['情人结'])
threads.append(t1)
t2 = threading.Thread(target=move,args=['姜子牙'])
threads.append(t2)

if __name__=='__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()    #当join与for并列，为多线程；当join与t并列，为单线程（join守护进程，子线程没结束，主线程不会结束）
    print("all over %s" %ctime())

