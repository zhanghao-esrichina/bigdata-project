'''
常用魔术方法

__init__  初始化对象成员
__new__   实例化
__call__  对象作为函数调用时触发
__del__   析构函数，当对象没有用（没有任何变量引用）的时候被触发
__str__   打印对象名，自动触发去调用__str__(self)里面的内容，类似C# override toString()方法，重载
'''


class Person:
    def __init__(self, name):
        print("---init---")
        print(self) 
        self.name = name

    def printName(self):
        print(self.name)

    def __new__(cls, *args, **kwargs):
        print("---new---")
        position = object.__new__(cls)
        print(position)
        return position


p = Person('zhanghao')
p.printName()
