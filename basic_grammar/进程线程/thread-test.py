#!/usr/bin/python3

import _thread
import time
import threading
from time import sleep
'''
状态：
新建>>就绪>>运行>>阻塞>>结束

优点：
（1）使用线程可以把占据长时间的程序中的任务放到后台去处理
（2）用户界面可以更加吸引人
（3）程序的运行速度更快
（4）在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用。在这种情况下我们可以释放一些珍贵的资源如内存占用等

threading.current_thread() 返回当前的线程变量
threading.active_count() 返回正则运行的线程数量，与len(threading.enumrate())有相同的结果
threading.enumerate() 返回一个包含正在运行的线程的list，正在运行指线程启动后、结束前、不包括启动前和终止后的线程
'''

# 线程可以共享全局变量
# 线程同步问题，锁，线程同步会减慢程序运行速度。python底层只要使用线程就会默认加锁（全局解释器锁 --> GIL）
# 进程，计算密集型。线程：耗时操作的时候，如网络下载，爬虫，文件IO


# 共享全局变量示例1:
m = 1000


def run1():
    global m
    for i in range(100):
        m -= 1


def run2():
    global m
    for i in range(100):
        m -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=run1, name='run1')
    t2 = threading.Thread(target=run2, name='run2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('m的值是：{0}'.format(m))

# 共享全局变量示例2:
n = 0


def task1():
    global n
    for i in range(1000000):
        n += 1

    print('task1中的n值是：{0}'.format(n))


def task2():
    global n
    for i in range(1000000):
        n += 1

    print('task2中的n值是：{0}'.format(n))


# if __name__ == "__main__":
#     th1 = threading.Thread(target=task1, name='task1')
#     th2 = threading.Thread(target=task2, name='task2')

#     th1.start()
#     th2.start()

#     th1.join()
#     th2.join()

#     print('n的值是{0}'.format(n))
#     print('over!!!')


# 使用_thread创建线程
# 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 0.3, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 1, ) )
# except:
#    print ("Error: 无法启动线程")

# while 1:
#    pass


# 使用threading创建线程

# def download(n):
#     images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
#     for image in images:
#         print('download: '+image)
#         sleep(n)
#         print('download {0} successful'.format(image))


# def listen_music():
#     musics = ['歌曲1', 'music2', 'music3', 'music4']
#     for music in musics:
#         sleep(0.5)
#         print('正在听 {}'.format(music))


# if __name__ == "__main__":
#     t = threading.Thread(target=download, name='aa', args=(1,))
#     t.start()

#     t2 = threading.Thread(target=listen_music, name='bb')
#     t2.start()

#     m = 1
#     while True:
#         sleep(3)
#         print(m)
#         m += 1
