import numpy as np
import pandas as pd


df = pd.read_csv(
    './CDNOW_master.txt',
    header=None,
    sep=r'\s+',
    names=[
        'user_id',
        'order_dt',
        'order_product',
        'order_amount'])
print(df)
print('\n order_dt列数据类型转换')
df['order_dt'] = pd.to_datetime(df['order_dt'], format='%Y%m%d')
print(df)

print('\n info')
print(df.info())
print(df.describe())