import numpy as np

x = [1, 2, 3]
a = np.asarray(x)
print(a)

x2 = (1, 3, 444)
print(np.asarray(x2))

# 设置dtype参数
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)


'''
numpy.frombuffer:

numpy.frombuffer 用于实现动态数组。
numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)

      注意：buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。
'''

s = b'hello world'
a = np.frombuffer(s, dtype='S1')
print(a)


'''
numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
numpy.fromiter(iterable, dtype, count=-1)

参数 	描述
iterable 	可迭代对象
dtype 	返回数组的数据类型
count 	读取的数据数量，默认为-1，读取所有数据
'''

list = range(5)
it = iter(list)
x = np.fromiter(it, dtype=float)
print(x)
print(x.shape)
print(x.ndim)

