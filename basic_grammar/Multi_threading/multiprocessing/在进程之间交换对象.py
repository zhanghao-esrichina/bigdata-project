# 队列是线程和进程安全的

from multiprocessing import Process, Pipe
from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()


# 管道 Pipe() 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）


# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()
