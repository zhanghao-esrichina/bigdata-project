
'''
进程间通讯
'''

from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]
    for image in images:
        print("正在下载： {0}".format(image))
        sleep(0.5)
        q.put(image)


def getfile(q):
    file = q.get()
    print("{0}保存成功！".format(file))


if __name__ == "__main__":
    q = Queue(5)
    t1 = Process(target=download, args=(q,))
    t2 = Process(target=getfile, args=(q,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('over!')
