from multiprocessing import Process
import os


def f(name):
    info('function f')
    print('hello', name)


def info(title):
    print(title)
    print('module name: ', __name__)
    print('parent process: ', os.getppid())  # 父进程id
    print('process id: ', os.getpid())   # 进程id


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()  # 调用start() 方法来生成进程
    p.join()
