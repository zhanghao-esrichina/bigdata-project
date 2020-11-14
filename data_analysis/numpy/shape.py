import numpy as np

'''
ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，其维度表示"行数"和"列数"。
'''

a = np.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (1, 6)  # shape和reshape函数都可以用来调整数组大小。
a2 = a.reshape(3, 2)
print(a2)

print(a2.shape)
print(a2.ndim)
