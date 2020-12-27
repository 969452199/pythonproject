import threading
from time import ctime,sleep
import time
class mytheard(threading.Thread):
    def __init__(self,second):
        threading.Thread.__init__(self)
        self.second = second


    def run(self):
        print(f'Threading {threading.current_thread().name} is running')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')
print(f'Threading {threading.current_thread().name} is running')

threads = []
if __name__=='__main__':
    for i in [1,5]:
        thread = mytheard(i)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Threading {threading.current_thread().name} is ended')


