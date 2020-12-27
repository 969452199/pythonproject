from multiprocessing import Process
import time
class myprocess(Process):
    def __init__(self,loop):
        Process.__init__(self)
        self.loop=loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'pid:{self.pid} LoopCount:{count}')

if __name__ == '__main__':
    for i in range(2,5):
        p = myprocess(i)
        p.start()

