import numpy as np
import pandas as pd


'''
DataFrame的创建：
- ndarray创建
- 字典创建

'''
df = pd.DataFrame(np.random.randint(100, size=(3, 4)))
print(df)
print(df.dtypes)

dic = {'name': ['zhangsan', 'lisi', 'wangwu'], 'salary': [1000, 2000, 5000]}
df2 = pd.DataFrame(data=dic, index=(1, 2, 3))
print(df2)
print(df2.index)
print(df2.values)
print(df2.shape)
print(df2.dtypes)
