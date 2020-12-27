import multiprocessing
def process(index):
    print(f'process:{index}')
# if __name__=='__main__':
#     for i in range(5):
#         p = multiprocessing.process(target=process,args=[i])
#         p.start()
if __name__=='__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process,args=(i,))
        p.start()