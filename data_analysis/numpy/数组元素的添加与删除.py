import numpy as np

'''
resize 	返回指定形状的新数组
append 	将值添加到数组末尾
insert 	沿指定轴将值插入到指定下标之前
delete 	删掉某个轴的子数组，并返回删除后的新数组
unique 	查找数组内的唯一元素
numpy.resize
'''

'''
numpy.resize 函数返回指定大小的新数组。

如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
numpy.resize(arr, shape)

参数说明：

    arr：要修改大小的数组
    shape：返回数组的新形状

'''
a = np.array([[1, 2, 3], [4, 5, 6]])
print('第一个数组：')
print(a)
print('第一个数组的shape：')
print(a.shape)
b = np.resize(a, (3, 2))
print(b)
print('第二个数组的形状：')
print(b.shape)
print('修改第二个数组的大小：')
b = np.resize(a, (3, 3))
print(b)

'''
numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外，输入数组的维度必须匹配否则将生成ValueError。

append 函数返回的始终是一个一维数组。

numpy.append(arr, values, axis=None)

参数说明：

    arr：输入数组
    values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
    axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行列数都要相同）。

'''
print('\n')
print('numpy.append 函数在数组的末尾添加值')
a = np.array([[1, 2, 3], [4, 5, 6]])
print('第一个数组：')
print(a)
print('第一个数组的shape：')
print(a.shape)
print('向数组中添加要素')
print(np.append(a, [7, 8, 9, ]))
print('沿轴0添加元素')
print(np.append(a, [[7, 8, 9]], axis=0))

print('沿轴1添加元素')
print(np.append(a, [[5, 5, 5, 5], [7, 8, 9, 10]], axis=1))


'''
numpy.insert

numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。

如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 此外，如果未提供轴，则输入数组会被展开。

numpy.insert(arr, obj, values, axis)

参数说明：

    arr：输入数组
    obj：在其之前插入值的索引
    values：要插入的值
    axis：沿着它插入的轴，如果未提供，则输入数组会被展开



'''
print('\n')
print('numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。')
a = np.array([[1, 2], [3, 4], [5, 6]])

print('第一个数组：')
print(a)
print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('传递了 Axis 参数。 会广播值数组来配输入数组。')
print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('沿轴 1 广播：')
print(np.insert(a, 1, [11], axis=1))


'''
numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。

Numpy.delete(arr, obj, axis)

参数说明：

    arr：输入数组
    obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
    axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开


'''
print('\n')
print('numpy.delete 函数返回从输入数组中删除指定子数组的新数组。')
a = np.arange(12).reshape(3, 4)

print('第一个数组：')
print(a)
print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('删除第一行')
print(np.delete(a, 0, axis=0))
print('删除第二列：')
print(np.delete(a, 1, axis=1))
print('包含从数组中删除的替代值的切片')
print(np.delete(a, np.s_[::2]))


'''
numpy.unique 函数用于去除数组中的重复元素。

numpy.unique(arr, return_index, return_inverse, return_counts)

    arr：输入数组，如果不是一维数组则会展开
    return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
    return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
    return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数

'''
print('\n')
print('numpy.unique 函数用于去除数组中的重复元素。')
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print('第一个数组：')
print(a)
print('第一个数组的去重值：')
print(np.unique(a))
print('新列表元素在旧列表中的位置（下标），并以列表形式储：')
u, indices = np.unique(a, return_index=True)
print(indices)
print('旧列表元素在新列表中的位置（下标），并以列表形式储：')
u, indices = np.unique(a, return_inverse=True)
print(u)
print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)
