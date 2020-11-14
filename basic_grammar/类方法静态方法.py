import time


class Dog:
    __age = 18

    def __init__(self, name):
        self.name = name

    def run(self):
        print("{}在院子里跑来跑去".format(self.name))

    @classmethod
    def test_classmethod(cls):
        print(cls)
        print(cls.__age)
        # print(cls.name)

    @classmethod
    def update_age(cls, new_age):
        cls.__age = new_age

    @classmethod
    def show_age(cls):
        print('年龄为：{}'.format(cls.__age))

    @staticmethod
    def test_staticmethod():
        print('----静态方法')
        print(Dog.__age)


Dog.update_age(30)
dog = Dog('范范')
dog.run()
Dog.test_classmethod()
Dog.test_staticmethod()
'''
# 类方法特点：
1.定义需要依赖装饰器@classmethod
2.类方法中参数不是一个对象，而是类
3.类方法只能使用类属性
4.类方法中不能使用对象方法
5.只能访问类属性和类方法，可以在对象创建之前，如果需要完成一些动作（功能），可以将此动作放在类方法中
'''

'''
# 静态方法特点：
1.需要装饰器@staticmethod
2.静态方法是无需传递参数（cls，self）
3.只能访问类的属性方法，对象的是无法访问的
4.加载时机与类方法相同


静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，
也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅
仅托管于某个类的名称空间中，便于使用和维护。

譬如，我想定义一个关于时间操作的类，其中有一个获取当前时间的函数。
'''


class TimeTest(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())
t = TimeTest(2, 10, 10)
nowTime = t.showTime()
print(nowTime)

'''
类方法

使用装饰器@classmethod。

原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更
合理，那么这个方法就可以定义为类方法。另外，如果需要继承，也可以定义为类方法。

如下场景：

假设我有一个学生类和一个班级类，想要实现的功能为：
    执行班级人数增加的操作、获得班级的总人数；
    学生类继承自班级类，每实例化一个学生，班级人数都能增加；
    最后，我想定义一些学生，获得班级中的总人数。
'''


class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''


a = Student()
b = Student()
print(ClassTest.getNum())
