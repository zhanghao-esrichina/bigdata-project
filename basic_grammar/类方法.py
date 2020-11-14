class Dog:
    __nickname = 'fanfan'

    @classmethod
    def set_nickname(cls, name):
        cls.__nickname = name
    '''
    类方法可以实现类似C#或Java里属性的功能，实现对类的变量的封装
    
    '''
    @classmethod
    def get_nickname(cls):
        return cls.__nickname

    @classmethod
    def printNickname(self):
        print(self.__nickname)

    def __init__(self, nickname):
        self.__nickname = nickname

    def run(self):
        print("{}在院子里跑来跑去".format(self.__nickname))

    @classmethod
    def test(cls):
        print(cls)
        print(cls.__nickname)


Dog.test()
Dog.set_nickname('zhanghao')
print(Dog.get_nickname())
Dog.printNickname()

dog = Dog('大黄')
dog.run()
