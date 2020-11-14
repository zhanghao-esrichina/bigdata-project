import numpy as np
import pandas as pd

df1 = pd.DataFrame(
    np.random.randint(
        0, 100, size=(
            5, 3)), columns=[
                'a', 'b', 'c'])
df2 = pd.DataFrame(
    np.random.randint(
        0, 100, size=(
            5, 3)), columns=[
                'a', 'd', 'c'])

df3 = pd.concat((df1, df2), axis=1)
print('\ndf3')
print(df3)
print('\ndf4')
df4 = pd.concat((df1, df2), axis=0)
print(df4)

print('\njoin表示级联的方式，outer inner')
print(pd.concat((df1, df2), axis=0, join='inner'))
print('\n外级联可以保证数据的完整性')
print(pd.concat((df1, df2), axis=0, join='outer'))
