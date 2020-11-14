import numpy as np

'''
numpy.empty(shape, dtype = float, order = 'C')

shape 	数组形状
dtype 	数据类型，可选
order 	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
'''
print("============x")
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
x = np.empty((3, 2), dtype=int)
print(x)

print("============x1")
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
x1 = np.array((3, 2), dtype=int)
print(x1)

# 创建指定大小的数组，数组元素以 0 来填充：numpy.ones表示数组元素用"1"来填充
x2 = np.zeros((3, 4), dtype=float, order='C')
print(x2)

# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=np.int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)
