import numpy as np

print("=============a1")
a1 = np.array([1, 2, 3, 4])
print(a1)

print("=============a2")
a2 = np.array([[1, 2], [3, 4]])
print(a2)

print('=============最小维度')
a3 = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a3)

a4 = np.array([1, 2, 3], dtype=complex)
print(a4)

dt = np.dtype(np.int32)
print(dt)