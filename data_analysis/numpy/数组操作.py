import numpy as np

'''
Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：

1.修改数组形状
reshape 	不改变数据的条件下修改形状
numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')

    arr：要修改形状的数组
    newshape：整数或者整数数组，新的形状应当兼容原有形状
    order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
'''
print('=====reshape 	不改变数据的条件下修改形状')
a = np.arange(8)
print('原始数组：')
print(a)
print('\n')

b = a.reshape(2, 4)
print('修改后的数组：')
print(b)

b2 = np.reshape(a, (4, 2), order='F')
print(b2)


'''

flat 	数组元素迭代器
'''
print('\n')
print('=====flat 	数组元素迭代器')
a = np.arange(9).reshape(3, 3)
print('原始数组：')
print(a)
print('row by row')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)

'''
flatten 	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
'''
print('\n')
print('=====flatten 	返回一份数组拷贝')
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
'''
ravel 	返回展开数组
numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
'''
print('\n')
print('=====ravel 	返回展开数组')
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))
print(a)


'''
    翻转数组
transpose 	对换数组的维度 numpy.transpose(arr, axes)
ndarray.T 	和 self.transpose() 相同
rollaxis 	向后滚动指定的轴
swapaxes 	对换数组的两个轴
'''
print('\n')
print('=====翻转数组')
a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))
print('T')
print(a.T)

'''
    修改数组维度
numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：

numpy.rollaxis(arr, axis, start)

参数说明：

    arr：数组
    axis：要向后滚动的轴，其它轴的相对位置不会改变
    start：默认为零，表示完整的滚动。会滚动到特定位置。

'''
print('\n')
print('=====修改数组维度')
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('获取数组中一个值：')
print(np.where(a == 6))
print(a[1, 1, 0])  # 为 6
print('\n')

# 将轴 2 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
b = np.rollaxis(a, 2, 0)
print(b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b == 6))
print('\n')

# 将轴 2 滚动到轴 1：（宽度到高度）

print('调用 rollaxis 函数：')
c = np.rollaxis(a, 2, 1)
print(c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c == 6))
print('\n')

'''
    连接数组
    分割数组
    数组元素的添加与删除


'''
