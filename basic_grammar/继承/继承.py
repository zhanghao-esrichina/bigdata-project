from os import sendfile

# 父类的私有变量不能被子类继承
class Person:
    def __init__(self) -> None:
        self.__money = 200
        self.name = '匿名'

    def show1(self):
        print(self.name, self.__money)


class Student(Person):
    def __init__(self, name, age):
        super().__init__() 
        # super(Student,self).__init__() 或者 Person.__init__(self) 都可以实现父类构造方法调用
        
        self.name = name
        self.age = age
        self.__money = 500

    def run(self):
        print(self.name+'正在跑步')

    def show(self):
        print('money:', self.__money)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name+'正在跑步')


class Doctor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name+'正在跑步')


s = Student('zhanghao', 30)
s.show()
s.show1()
