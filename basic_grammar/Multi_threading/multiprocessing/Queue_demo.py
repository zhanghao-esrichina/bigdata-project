from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


def func(q):
    for i in range(5):
        q.put(i)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=(q,))
    p.start()
    print(q.get())
    p.join()
