import numpy as np

a = np.arange(24)
print(a)
print(a.ndim)

a2 = a.reshape(2, 4, 3)  # 最外围是2，两个分段分别是4行3列的数组
a3 = a.reshape(3, 2, 4)
print(a2)
print(a3)
print(a2.ndim)
print(a3.ndim)

# shape元组的长度与rank或维度的个数是一致的
print("=========shape")
print(a2.shape)
print(a3.shape)

# sizes数组元素的总数，等于shape的元素的乘积
print(a2.size)  # 2*4*3

# itemsize表示数组中每个元素的字节大小
print(a2.itemsize)

print(a2.data)
