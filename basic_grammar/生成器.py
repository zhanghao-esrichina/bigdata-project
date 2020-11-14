'''
通过列表推导式，我们可以直接创建一个列表，但是受到内存限制，列表容量是有限的，而且创建一个包含100万个元素的列表，不仅占用很大的储存空间，
如果我们仅仅需要访问前面几个元素，那后面的绝大多数元素占用的空间都是白白浪费了，所以，如果列表元素可以按照某种算法推算出来，那我们是否可
以中循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在python中，这种一边循环一边计算的机制，称为生成器，
“generator”

得到生成器的方式：
1.通过列表推导式得到生成器
2.
'''


newlist = [x for x in range(5)]
print(newlist)

# 生成器使用小括号“()”
g = (x for x in newlist)

while True:
    try:
        e = next(g)
        print(e)
    except Exception as e:
        print('没有更多元素了！')
        break

# 只要函数中出现了关键字yield，说明函数就不是函数，为“生成器！！！”
# 调用函数，接收函数的结果分别借助于 __next()__或next()


def func():
    n = 0
    while True:
        n += 1
        yield n


# g = func()
# print(next(g))
# print(next(g))
# print(next(g))

# 斐波拉契函数
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a+b
        n += 1


# g2 = fib(10)
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())


'''
生成器方法：
    __next__() 获取下一个元素
    send(value) 向每次生成器中传值，第一次调用send(None)
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)

        for i in range(temp):
            print("---------->", i)
        print('***************')
        i += i
    return '没有更多的数据'


g = gen()

print(g.send(None))
n1 = g.send(3)
print('n1:', n1)
n2 = g.send(5)
print('n2:', n2)
