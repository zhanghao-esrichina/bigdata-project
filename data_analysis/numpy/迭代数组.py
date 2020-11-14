import numpy as np

'''
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。

迭代器最基本的任务的可以完成对数组元素的访问。

'''


a = np.arange(6).reshape(2, 3)
print('原始数组：')
print(a)
print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=',')
print('\n')

#  a.T.copy(order = 'C') 的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。
print("转置按行优先迭代")
for x in np.nditer(a.T.copy(order='C')):
    print(x, end=',')
print('\n')

print("C order，即是行序优先")
for x in np.nditer(a, order='C'):
    print(x, end=',')
print('\n')

print("按列序优先迭代")
for x in np.nditer(a, order='F'):
    print(x, end=',')
'''
控制遍历顺序

    for x in np.nditer(a, order='F'):Fortran order，即是列序优先；
    for x in np.nditer(a.T, order='C'):C order，即是行序优先；

'''
print('\n')

print('===========================================')
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('原始数组的转置是：')
b = a.T
print(b)
print('\n')
print('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=", ")

print('\n')
print("===============修改数组中元素的值=======================")
'''
nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），为了在遍历数组的同时，
实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。
'''

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)

print("=======================使用外部循环==============================")
'''
使用外部循环

nditer类的构造器拥有flags参数，它可以接受下列值：
c_index 	可以跟踪 C 顺序的索引
f_index 	可以跟踪 Fortran 顺序的索引
multi-index 	每次迭代可以跟踪一种索引类型
external_loop 	给出的值是具有多个值的一维数组，而不是零维数组
'''

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('修改后的数组是：')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=", ")

print("\n")
print("====================广播迭代====================")
'''
 广播迭代

如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。
'''

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('\n')
print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')
print('修改后的数组为：')
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=", ")
