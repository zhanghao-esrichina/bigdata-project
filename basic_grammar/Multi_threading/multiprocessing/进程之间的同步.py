
from multiprocessing import Process, Lock


def f(i):
    print('hello world', i)



if __name__ == '__main__':
    for num in range(10):
        Process(target=f, args=(num,)).start()



# 可以使用锁来确保一次只有一个进程打印到标准输出:

# def f(l, i):
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()
