import numpy as np

'''
NumPy 提供了很多统计函数，用于从数组中查找最小元素，最大元素，百分位标准差和方差等。 函数说明如下：
numpy.amin() 和 numpy.amax()

numpy.amin() 用于计算数组中的元素沿指定轴的最小值。
numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
'''
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('我们的数组是：')
print(a)
print('调用 amin() 函数：')
print(np.amin(a))
print('调用 amax() 函数：')
print(np.amax(a))
print('再次调用 amax() 函数,axis=0：')  # axis=0，则沿着纵轴进行操作
print(np.amax(a, axis=0))
print('再次调用 amax() 函数,axis=1：')  # axis=1，则沿着横轴进行操作
print(np.amax(a, axis=1))

'''
关于axis用法的小技巧：
>>> import numpy as np
>>> data = np.array([
... [1,2,1],
... [0,3,1],
... [2,1,4],
... [1,3,1]])
设axis=i，则numpy沿着第i个下标变化的方向进行操作。例如刚刚的例子，可以将表示为：data =[[a00, a01],[a10,a11]]，
所以axis=0时，沿着第0个下标变化的方向进行操作，也就是a00->a10, a01->a11，也就是纵坐标的方向，axis=1时也类似。
'''
'''
numpy.ptp()
numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。
'''
print('\n')
print('ptp()函数计算数组中元素最大值与最小值的差')
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('我们的数组是：')
print(a)
print('调用 ptp() 函数：')
print(np.ptp(a))
print('沿轴 1 调用 ptp() 函数：')
print(np.ptp(a, axis=1))
print('沿轴 0 调用 ptp() 函数：')
print(np.ptp(a, axis=0))
print('\n')

'''
numpy.median()
numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
'''
print('median() 函数用于计算数组 a 中元素的中位数（中值）')
a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print('我们的数组是：')
print(a)
print('调用median()函数：')
print(np.median(a))
print('沿轴0调用median()函数：')
print(np.median(a, axis=0))
print('沿轴1调用median()函数：')
print(np.median(a, axis=1))
print('\n')

'''
numpy.mean()

numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。
算术平均值是沿轴的元素的总和除以元素的数量。
'''
print('numpy.mean() 函数返回数组中元素的算术平均值。')
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('我们的数组是：')
print(a)
print('调用 mean() 函数：')
print(np.mean(a))
print('沿轴 0 调用 mean() 函数：')
print(np.mean(a, axis=0))
print('沿轴 1 调用 mean() 函数：')
print(np.mean(a, axis=1))
print('\n')

'''
numpy.average()

numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。
该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。
加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。
考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
'''
a = np.array([1, 2, 3, 4])
print('我们的数组是：')
print(a)
print('调用 average() 函数：')
print(np.average(a))
# 不指定权重时相当于 mean 函数
wts = np.array([4, 3, 2, 1])
print('再次调用 average() 函数：')
print(np.average(a, weights=wts))
# 如果 returned 参数设为 true，则返回权重的和
print('权重的和：')
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 2], returned=True))


'''
标准差是一组数据平均值分散程度的一种度量。
标准差是方差的算术平方根。
标准差公式如下：
std = sqrt(mean((x - x.mean())**2))

方差
统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。
换句话说，标准差是方差的平方根。
'''
print('sqrt 标准差是一组数据平均值分散程度的一种度量。')
print(np.std([1, 2, 3, 4]))
print(np.var([1, 2, 3, 4]))
