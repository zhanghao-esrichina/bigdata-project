class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+' is now sitting')

    def roll_over(self):
        print(self.name.title() + ' rolled over')


if __name__ == "__main__":
    myDog = Dog('kone chuang', 33)
    print('my dog name is :'+myDog.name)
    print('my dog age:' + str(myDog.age))
