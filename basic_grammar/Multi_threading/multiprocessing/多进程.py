
# =====================new Process=======================================
from multiprocessing import Process, Queue
import subprocess
import random
import time
from multiprocessing import Pool
from multiprocessing import Process
import os

# 子进程要执行的代码


# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# =====================new Process=======================================
# print("=====================Pool=======================================")


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#
# print("=====================subprocess=======================================")
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)


'''
进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、
Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''
print('=====================进程间通信=====================')
def write(q):
    print('Process tp write:{0}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put {0} to queue'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read {0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get {0} from queue'.format(value))


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
