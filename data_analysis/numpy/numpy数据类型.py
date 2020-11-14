'''
每个内建类型都有一个唯一定义它的字符代码，如下：
字符 	对应类型
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


import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)



import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)

'''