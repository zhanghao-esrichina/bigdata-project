'''
死锁
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。

解决：
1.重构代码
2.acquiree加timeout参数解决
'''
import threading
import time


lockA = threading.Lock()
lockB = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        if lockA.acquire():
            print(self.name+'获取了A锁')
            time.sleep(0.5)
            if lockB.acquire(timeout=3):
                print(self.name+'有获取了B锁，原来还有A锁')

                lockB.release()
            lockA.release()


class MyThread1(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        if lockB.acquire():
            print(self.name+'获取了B锁')
            time.sleep(0.5)
            if lockA.acquire(timeout=3):
                print(self.name+'有获取了A锁，原来还有B锁')

                lockA.release()
            lockB.release()


if __name__ == "__main__":
    t1 = MyThread('线程1： ')
    t2 = MyThread1('线程2： ')

    t2.start()
    t1.start()
