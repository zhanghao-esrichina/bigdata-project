import numpy as np
import pandas as pd

dic = {
    'time': [
        '2020-10-10',
        '2020-10-11',
        '2020-10-12'],
    'temp': [
        33,
        31,
        30]}
df = pd.DataFrame(data=dic)
print(df)

print('time列类型：')
print(df.columns)
print(df['time'].dtypes)

print("\n")
print('类型转换：')
df['time'] = pd.to_datetime(df['time'])
print(df.info())
