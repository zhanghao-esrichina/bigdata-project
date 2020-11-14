

from os import name


class Article:
    __name = ''
    def __init__(self, name):
        self.__name = name

    def show(self):
        print('article', self.__name)
