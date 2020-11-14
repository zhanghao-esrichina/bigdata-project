class People(object):
    # 类属性是指定义在类的内部而且在方法的外部的属性
    money = 10000

    def __init__(self, name, age, gender=1):
        # 对象属性是指定义在方法的内部的属性，例如本例中
        # name，age和gender都是对象属性
        self.name = name
        self.age = age
        self.gender = gender


# 创建两个类的对象
student1 = People("张三", 20)
student2 = People("李四", 25)

# 类属性和对象属性的区别：


# 对象可以通过  对象名.属性名  调用对象属性和类属性
print(student2.name)
print(student2.money)

# 而类也可以通过  类名.属性名  调用类的属性，但是
# 不能通过这种方式调用对象的属性
# 例如类调用name属性，会报异常
# AttributeError: type object 'People' has no attribute 'name'
print(People.money)
# print(People.name)

# 类属性和对象属性在使用上的区别：


# 在进行运算前这三个引用的都是类属性money
# 所以这三个的属性money的内存地址都是相同的
print(id(student1.money))
print(id(student2.money))
print(id(People.money))

student1.money = student1.money-1000
People.money -= 1000
# 再打印三者的内存地址
print(id(student1.money))
print(id(student2.money))
print(id(People.money))

# 当student2进行同样的运算后，那么student2中也会创建一个money属性
# 此时三者的money属性的内存地址都不一样了
student2.money -= 1000
print(id(student1.money))
print(id(student2.money))