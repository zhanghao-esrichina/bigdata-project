import numpy as np


# dt = np.dtype([('age', np.int8)])
# print(dt)

print("=========将数据类型应用于 ndarray 对象")
dt2 = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt2)
print(a)


print("==========# 类型字段名可以用于存取实际的 age 列")
dt3 = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt3)
print(a['age'])


'''
定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
'''

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a2 = np.array([('zhangsan', 21, 50), ('lisi', 18, 75)], dtype=student)
print(a2)



# 数组元素的总个数，相当于 .shape 中 n*m 的值
print("size:",a2.size)
# 数组的维度，对于矩阵，n 行 m 列
print("shape:",a2.shape)
# 秩，即轴的数量或维度的数量
print("ndmin:",a2.ndim)
# ndarray 对象的元素类型
print("dtype:",a2.dtype)

# ndarray 对象的内存信息
print("flags:",a2.flags)


'''
b	布尔型
i	(有符号) 整型
u 	无符号整型 integer
f	浮点型
c 	复数浮点型
m 	timedelta（时间间隔）
M 	datetime（日期时间）
O 	(Python) 对象
S, a 	(byte-)字符串
U	Unicode
V 	原始数据 (void)
'''