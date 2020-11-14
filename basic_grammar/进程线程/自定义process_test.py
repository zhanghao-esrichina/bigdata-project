from logging import setLogRecordFactory, setLoggerClass
from multiprocessing import Process
from os import name


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        n = 1
        while True:
            print('{}------------自定义进程：{}'.format(n, self.name))
            n += 1


if __name__ == "__main__":
    my_process = MyProcess('小明')
    my_process.start()

    my_process2 = MyProcess('子骞')
    my_process2.start()
