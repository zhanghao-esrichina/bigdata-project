import random as rd

def newRUN(fn):
    ns = []
    for i in range(10):
        n = round(rd.random(), 2)
        ns.append(n)

    fn(ns)


def abc(*args):
    print('生成数据成功')
    print(args)

newRUN(abc)