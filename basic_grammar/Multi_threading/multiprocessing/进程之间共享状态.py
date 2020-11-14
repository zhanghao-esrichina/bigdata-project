from multiprocessing import Process, Manager
from multiprocessing import Process, Value, Array

# 共享内存：可以使用 Value 或 Array 将数据存储在共享内存映射中

#
# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#
#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])

# 服务器进程：由 Manager() 返回的管理器对象控制一个服务器进程，该进程保存Python对象并允许其他进程使用代理操作它们。
# 服务器进程管理器比使用共享内存对象更灵活，因为它们可以支持任意对象类型。此外，单个管理器可以通过网络由不同计算机上的进程共享。但是，它们比使用共享内存慢。

def f(d, l):
    d[1] = '1'
    d[2] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
