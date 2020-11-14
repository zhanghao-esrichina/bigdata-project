import functools
import logging
import decorator

# def today():
#     print('2020-09-27')
#
# def today():
#     print('2020-09-27')
#     logging.info('today is running...')

'''
如果函数 yesterday()、tomorrow() 也有类似的需求，怎么做？再写一个 logging 在yesterday函数里？这样就造成大量雷同的代码，为了减少重复
写代码，我们可以这样做，重新定义一个新的函数：专门处理日志 ，日志处理完之后再执行真正的业务代码
'''


# def logging_tool(func):
#     func()
#     logging.info('%s is running...' % func.__name__)
#
#
# def today():
#     print('2020-09-27')
#
#
# logging_tool(today)
'''
这样做逻辑上是没问题的，功能是实现了，但是我们调用的时候不再是调用真正的业务逻辑today函数，而是换成了logging_tool函数，这就破坏了原有的
代码结构，为了支持日志功能，原有代码需要大幅修改，那么有没有更好的方式的呢？当然有，答案就是装饰器。

'''


# def logging_tool(func):
#     def wrapper(*args, **kwargs):
#         logging.info('%s is running...' % func.__name__)
#         func()
#     return wrapper
#
#
# def print_today():
#     print('2020-09-27')
#
#
# today = logging_tool(print_today)
# today()

'''
@语法糖
接触 Python 有一段时间的话，对 @ 符号一定不陌生了，没错 @ 符号就是装饰器的语法糖，它放在函数开始定义的地方，这样就可以省略最后一步
再次赋值的操作.有了 @ ，我们就可以省去today = logging_tool(today)这一句了，直接调用 today() 即可得到想要的结果。
不需要对today() 函数做任何修改，只需在定义的地方加上装饰器

'''


# def logging_tool(func):
#     def wrapper(*arg, **kwargs):
#         logging.info('%s is running...' % func.__name__)
#         func()  # 把today当作参数传递进来，执行func()就相当于执行today()
#     return wrapper
#
#
# @logging_tool
# def today():
#     print('2020-09-27')
#
#
# today()


'''
装饰器本质上是一个Python函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外的功能，装饰器的返回值也是一个函数/类对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计。
有了装饰器，我们就可以抽离出大量与函数功能本身无关的代码到装饰器中并继续重用。
简单来说：装饰器的作用就是让已经存在的对象添加额外的功能。

'''

# 1.带参数的装饰器


# def logging_tool(level, name):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == 'error':
#                 print('%s is running...' % func.__name__)
#             elif level == 'warn':
#                 print('%s is running...' % func.__name__)
#             else:
#                 print('%s is running...' % func.__name__)
#             func(name)
#         return wrapper
#     return decorator
#
#
# @logging_tool(level='error', name='zhanghao')
# def today(name):
#     print('hello, {0}!Today is {1}'.format(name, '2020-09-27'))
#
#
# today(name="zhanghao")


# 2.让装饰器同时支持带参数或不带参数


# def new_logging_tool(obj):
#     if isinstance(obj, str):
#         def decorator(func): # 带参数的情况，参数类型为str
#             @functools.wraps(func)
#             def wrapper(*args, **kwargs):
#                 if obj == 'error':
#                     logging.error('%s is running...' % func.__name__)
#                 elif obj == 'warn':
#                     logging.warning('%s is running...' % func.__name__)
#                 else:
#                     logging.info('%s is running...' % func.__name__)
#                 func()
#             return wrapper
#         return decorator
#     else:  # 不带参数的情况，参数类型为函数类型，即被装饰的函数
#         @functools.wraps(obj)
#         def wrapper(*args, **kwargs):
#             logging.info('%s is running...' % obj.__name__)
#             obj()
#
#         return wrapper
#
#
# @new_logging_tool
# def yesterday():
#     print('2018-05-24')
#
#
# yesterday()
#
#
# @new_logging_tool('warn')
# def today(name='devin'):
#     print('Hello, %s! Today is 208-05-25' % name)
#
#
# today()


# 3.类装饰器
'''
装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的call方法，
当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
'''

# 示例一、被装饰函数不带参数

# class Foo(object):
#     def __init__(self, func):
#         self._func = func  # 初始化装饰的函数
#
#     def __call__(self):
#         print('class decorator running')
#         self._func()
#         print('class decorator ending')
#
#
# @Foo
# def bar():
#     print('bar')
#
#
# bar()

# 示例二、被装饰函数带参数

# class Counter:
#     def __init__(self, func):
#         self._func = func
#         self.count = 0  # 记录函数被调用的次数
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self._func(*args, **kwargs)
#
#
# @Counter
# def today(name='devin'):
#     print('Hello, %s! Today is 208-05-25' % name)  # 被装饰的函数带参数的情况
#
#
# for i in range(10):
#     today()
# print(today.count)  # 10

# 示例三、不依赖初始化函数，单独使用call函数实现（体现类装饰器灵活性大、高内聚、封装性高的特点）


class LogTool(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):  # __call__作为装饰器函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)

            with open(self.logfile, 'a') as fw:
                fw.write(log_string + '\n')  # 保存日志
            self.notify()  # 发送通知
            return func(*args, **kwargs)
        return wrapper()

    def notify(self):
        pass


class EmailTool(LogTool):
    # LogTool的子类，实现email通知功能，在函数调用时发送email给用户
    def __init__(self, email='767802022@qq.com', *args, **kwargs):
        self.email = email
        super(EmailTool, self).__init__(*args, **kwargs)

    # 覆盖父类的通知功能，实现发送一封email到self.email
    def notify(self):
        pass


@EmailTool()  # 单独使用__call__函数实现时，别忘了添加括号，进行类的初始化
def bill_func():
    pass


# 给一个已有的类添加长度属性和getter、setter方法

def Length(cls):
    class NewClass(cls):
        @property
        def length(self):
            if hasattr(self, '__len__'):
                self._length = len(self)
            return self._length

        @length.setter
        def length(self, value):
            self._length = value
    return NewClass


@Length
class Tool(object):
    pass


t = Tool()
t.length = 10
print(t.length)


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value


s = Student()
s.score = 95
print(s.score)
s.score = 999
print(s.score)
