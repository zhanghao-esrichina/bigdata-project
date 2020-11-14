class Presenter(object):
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print('hello '+self.name)