#私有属性和私有方法只能内部调用（用下划线）
#set...守护进程
import threading   #引入线程函数
import time
def target1(second):
    print(f'Threading {threading.current_thread().name} is running')  #主线程开始运行
    print(f'Threading {threading.current_thread().name} sleep {second}s')   #子线程1运行
    time.sleep(second)                                                 #子线程1等待1秒，接着子线程开始运行
    print(f'Threading {threading.current_thread().name} is ended')   #主线程运行结束
print(f'Threading {threading.current_thread().name} is running')
for i in [1,5]:   #两个参数，2个线程
    thread = threading.Thread(target=target1,args=[i])
    thread.start()
print(f'Threading {threading.current_thread().name} is ended')







