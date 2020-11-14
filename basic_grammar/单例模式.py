# 每个类只能创建一个实例


class Singleton:
    __instance = None

    # 重写__new__
    def __new__(cls):
        print('---------__new')
        if cls.__instance is None:
            # cls.__instance = object.__init__(cls)
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


s = Singleton()
s1 = Singleton()

print(id(s))
print(id(s1))
