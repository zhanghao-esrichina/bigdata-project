'''
共享数据
如果多个线程对某个数据进行修改，则可能出现不可预料对结果，为了保证数据的正确性，需要对多个线程进行同步，一个一个的完成。

使用thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间

'''

import threading
import random
import time

lock = threading.Lock()
list1 = [0]*10


def set_list_value():
    # 获取线程锁，如果已经上锁则等待释放
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)

    lock.release()


def get_list_value():
    lock.acquire()
    for i in range(len(list1)):
        print("===== ", list1[i])
        time.sleep(0.5)

    lock.release()


if __name__ == "__main__":
    get_task = threading.Thread(target=get_list_value)
    set_task = threading.Thread(target=set_list_value)

    get_task.start()
    set_task.start()

    get_task.join()
    set_task.join()

    print(list1)


