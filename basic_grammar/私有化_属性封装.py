'''
私有化

封装、继承、多态
封装：1.私有化属性 2.定义公有set和get方法
'''


class Students:
    __score = 0
    __age = 0

    def __init__(self, name):
        self.name = name

    def set_score(self, score):
        self.__score = score

    def get_score(self, score):
        return self.__score

    # 先用装饰器定义某变量的get，再定义xxx.setter装饰器
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def __str__(self):
        return "姓名：{},年龄{},分数{}".format(self.name, self.age, self.__score)


student = Students('kone')
student.age = 25
student.set_score(80)
print(student)
# print(__name__)
print(student.__dir__())
