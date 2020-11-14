import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 100, size=(8, 6)))
df.iloc[2, 3] = None
df.iloc[4, 4] = None
df.iloc[5, 2] = None
print(df)

# 对空值进行过滤
print(df.isnull())

# 哪些行中存在true值？
print(df.isnull().any(axis=1))
print(df.isnull().any(axis=0))

# 将上部对布尔值作为源数据对行索引
print('drop index')
drop_index = df.loc[df.isnull().any(axis=1)].index
print(drop_index)
print('将缺失数据对行进行删除')
print(df.drop(labels=drop_index, axis=0))
print('\n')
print('使用all函数判断整行都为true')
print(df.notnull().all(axis=1))

print('使用all函数判断整列都为true')
print(df.notnull().all(axis=0))
'''
判断规则：
isnull any
notnull all 结合使用
'''

print('\n')
print('使用dropna')
print(df.dropna(axis=0))
print('\n')
print('对缺失值进行覆盖')
'''
fillna

'''
print(df)
print(df.fillna(method='ffill', axis=0))
