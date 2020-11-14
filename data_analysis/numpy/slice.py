import numpy as np
'''
ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。

ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。

'''
a = np.arange(10)
print(a)

s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
print(a[s])


# 通过冒号分隔切片参数 start:stop:step 来进行切片操作

print(a[2:7:2])
print(a[2:9:3])
print(a[2:])
print(a[2:5])


# 多维数组同样适用于上述索引提取方法
a2 = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a2)

print("从数组索引a[1:]处开始切割")
print(a2[1:])

# 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。
a3 = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a3[..., 1])  # 第二列元素
print(a3[1, ...])  # 第二行元素
print(a3[..., 1:])  # 第二列及剩下的所有元素
