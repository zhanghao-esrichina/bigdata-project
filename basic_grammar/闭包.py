
# 内部函数可以访问外部函数的变量
# 内部函数可以修改外部函数的可变类型变量
# 内部函数修改全局的不可变变量值时，需要在内部函数中将其声明为“global”，内部变量修改外部函数的不可变变量，需要在内部函数中将其声明为“nonlocal”
# locals()查看本地变量有哪些，globals()查看全局变量有哪些，都是以字典的形式输出

import time

print("demo1=================")


def func():
    n = 100
    list1 = [3, 6, 9, 4]

    def inner_func():
        nonlocal n

        # 遍历只是取出列表中的各个值，为新的对象，另外开辟内存进行存储
        # for i in list1:
        #     i+=5

        # for index, i in enumerate(list1):
        #     list1[index] = i+5
        for i in range(len(list1)):
            list1[i] += 5

        list1.sort()

        n += 100

    inner_func()
    print(list1)
    print(n)


func()
print("\n")
print("demo1=================")
# 全局变量
a = 100
# 定义函数


def func2():
    b = 100

    print(a, id(a))
    print(b, id(b))
    # 内部函数

    def inner_func2():
        nonlocal b
        global a
        c = 100
        a += 1
        b += 2
        print(a, id(a))
        print(b, id(b))
        print(c, id(c))

    inner_func2()
    # locals()可以查看当前函数中声明的内容
    print(locals())
    print(globals())


func2()

print("\n")
print("闭包=================")
# 外部函数中定义了内部函数
# 外部函数有返回值
# 返回值是：内部函数名
# 内部函数引用了外部函数的变量


def func3():
    a = 100

    def inner_func3():
        b = 200
        print(a, b)

    return inner_func3


x = func3()
x()

print("\n")
print("闭包实现统计访问=================")


def func4():
    a = 100

    def func4_inner1():
        b = 90
        s = a+b
        print(s)

    def func4_inner2():
        nonlocal a
        a = 200
        func4_inner1()

    return func4_inner2


f4 = func4()
print(f4)
f4()


print("\n")
print("定义装饰器=================")

# 装饰器与普通闭包的区别在于，外部函数传入的参数为“函数”


def func_decorate(a):
    a = a+1
    print(a)


def decorate1(func5):
    a = 100

    def wrapper():
        print("=====111111111")
        func5()
        print("=====222222222")
        print(a+1)

    return wrapper


# f = decorate1(func_decorate)
# f()

# 1.func_decorate2为被装饰函数
# 2.将被装饰函数作为参数传递给装饰器”decorate1“
# 3.执行decorate1函数
@decorate1
def func_decorate2():
    a = 1000
    print(a)


func_decorate2()

print("\n")
print("装饰器应用，模拟登陆验证=================")


def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123':
        return True
    else:
        return False


islogin = False


def login_required(func5):
    def wrapper(*args, **kwargs):
        global islogin
        if islogin:
            func5(*args, **kwargs)
        else:
            # print("挑战到登陆页面")
            islogin = login()
            print('result:{}'.format(islogin))
    return wrapper


@login_required
def pay(money):
    print("正在付款，付款金额是{}元".format(money))
    print("付款中")
    time.sleep(2)
    print('付款完成')


pay(1)
pay(10000)
