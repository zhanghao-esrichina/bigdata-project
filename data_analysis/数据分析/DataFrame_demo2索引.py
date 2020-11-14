import numpy as np
import pandas as pd

df = pd.DataFrame(
    data=np.random.randint(
        6, 100, size=(
            8, 4)), columns=[
                'a', 'b', 'c', 'd'])
print(df)

print("# 单行")
print(df.iloc[0])
print("# 多行")
print(df.iloc[[0, 3, 5]])
print(df.iloc[0:2])
print("# 单列")
print(df['a'])
print("# 多列")
print(df[['a', 'b']])

print('# 取单个元素')
print(df.iloc[0, 2])
print(df.loc[0, 'a'])
print('# 取多个元素')
print(df.loc[[0, 1], 'a'])
print(df.loc[0:3, 'a'])
print(df.iloc[:, 0:2])
