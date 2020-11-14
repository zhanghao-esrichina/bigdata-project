import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        run_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以速度{}行驶了{}小时'.format(
            self.brand, road.name, self.speed, run_time)

        print(msg)

    def __str__(self):
        return '{}品牌的，速度{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('独库公路', 100)
audi = Car('奥迪', 220)
audi.get_time(r)
