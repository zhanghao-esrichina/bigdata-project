'''


广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。

'''

# 如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b
# 数组对应位相乘。这要求维数相同，且各维度的长度相同。
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)


print('当运算中的2个数组shape不同时，numpy将自动触发广播机制')
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([[1, 2, 3]])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度,行复制为原来的4倍
bbb = np.tile(b, (1, 4))  # 列复制为原来的四倍

print("a+b")
print(a + b)
print("bb")
print(bb)
print('bbb')
print(bbb)
print("a+bb")
print(a + bb)

# 关于tile函数用法
'''
np.ones((2,3)) 等效于 np.tile(1., (2,3))

np.zeros((2,3)) 等效于 np.tile(0., (2,3)) 
'''