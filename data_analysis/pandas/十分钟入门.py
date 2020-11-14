import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20201022', periods=6)
print(dates)

df = pd.DataFrame(
    np.random.randint(
        100,
        size=(
            6,
            4)),
    index=dates,
    columns=list('abcd'))
print(df)

# print(np.random.randint(10,size=(2,3)))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20201022'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
df3 = df2.copy()
print(df2.E)

print('\n')
print('DataFrame dtypes')
print(df2.dtypes)
print('\n')
print('DataFrame head')
print(df2.head(1))
print('\n')
print('DataFrame tail')
print(df2.tail(2))
print('\n')
print('DataFrame index')
print(df2.index)
print('\n')
print('DataFrame columns name')
print(df2.columns)

'''
DataFrame 的列由多种数据类型组成时，该操作耗费系统资源较大，这也是 Pandas 和 NumPy 的本质区别：NumPy 数组只有一种数据类型，
DataFrame 每列的数据类型各不相同。调用 DataFrame.to_numpy() 时，Pandas 查找支持 DataFrame 里所有数据类型的 NumPy 数据类型。
还有一种数据类型是 object，可以把 DataFrame 列里的值强制转换为 Python 对象。


DataFrame.to_numpy() 的输出不包含行索引和列标签。
'''

print('\n')
print('pandas转numpy')
np1 = df2.to_numpy()
print(np1)
print(np1.dtype)

print('\n')
print('DataFrame df')
print(df)
print('\n')
print('DataFrame describe')
print(df.describe())
print('\n')
print('DataFrame 转置数据')
print(df.T)
print('\n')
print('DataFrame 按轴排序')
print(df.sort_index(axis=1, ascending=True))  # 按行进行大小排序
print('\n')
print('DataFrame 按值排序')
print(df.sort_values(by='b'))

print('\n')
print('从DataFrame中取数据：')
print(df['a'])
print(df[0:3])
print(df['20201022':'20201023'])

print('\n')
print('按标签选择')
print('用标签提取一行数据')
print(df.loc[dates[0]])  # 取的第一行数据
print('用标签选择多列数据')
print(df.loc[:, ['a', 'd']])
print('用标签切片，包含行与列结束点')
# DataFrame的loc函数可以实现分别在行和列上截取数据
print(df.loc['20201022':'20201023', ['a', 'b']])
print('返回对象降维')
print(df.loc['20201022', ['a', 'b']])
print('提取标量值')
print(df.loc['20201022', 'a'])
print('快速访问标量')
print(df.at['20201022', 'a'])

print('\n')
print('按位置选择')
print(df.iloc[3])  # 选择的是index 行
print('类似 NumPy / Python，用整数切片：')
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
print('显式整行切片：')
print(df.iloc[1:3, :])
print('显示整列切片')
print(df.iloc[:, 1:3])
print('显式提取值')
print(df.iloc[1, 1])

print('\n')
print('布尔索引')
print('用单列的值选择数据：')
print(df[df.a > 50])
print('选择DataFrame里面值满足条件的：')
print(df[df > 50])
print(df > 50)
print('用 isin() 筛选：')
df3 = df.copy()
df3['e'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df3)
print(df3[df3['e'].isin(['two', 'four', 'python'])])

print('\n')
print('赋值')
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20201022', periods=6))
print(s1)
print('用索引自动对齐新增列的数据：')
df['f'] = s1
print(df)
print('按标签赋值：')
df.at['20201022', 'a'] = 0
print(df)
print('按位置赋值:')
df.iat[0, 3] = 0
print(df)
print('按 NumPy 数组赋值：')
df.loc[:, 'd'] = 999
print(df)
print('用 where 条件赋值：')
df[df == 999] = 888
print(df)

print('\n')
print('缺失值')
'''
Pandas 主要用 np.nan 表示缺失数据。 计算时，默认不包含空值。详见缺失数据。
重建索引（reindex）可以更改、添加、删除指定轴的索引，并返回数据副本，即不更改原数据。
'''
df5 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['e'])
df5.loc[dates[0]:dates[1], 'e'] = 1
print(df5)
print('删除所有含缺失值的行：')
print(df5.dropna(how='any'))
print('填充缺失值：')
print(df5.fillna(value=5))
print('提取nan值的布尔掩码')
print(pd.isna(df5))

print('\n')
print('运算')
print(df)
print(df.mean())
print(df.mean(1))
print('不同维度对象运算时，要先对齐。 此外，Pandas 自动沿指定维度广播。')
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
df.sub(s, axis='index')
print(df)

print('\n')
print('字符串')
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())
print(s.str.upper())


print('\n')
print('DataFrame的拆分合并')
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
print('拆分')
pieces = [df[:3], df[3:7], df[9:]]
print(pieces)
print('合并')
print(pd.concat(pieces))

print('\n')
print('连接join')
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(pd.merge(left, right, on='key'))

print('\n')
print('追加')
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
print(df.append(s, ignore_index=True))

print('\n')
print('分组（Grouping）')
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)
print(df.groupby('A').sum())
print('多列分组后，生成多层索引，也可以应用 sum 函数：')
print(df.groupby(['A', 'B']).sum())

print('\n')
print('Reshaping重塑')
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df[:4])
print('stack() 方法把 DataFrame 列压缩至一层：')
print(df[:4].stack())

print('\n')
print('数据透视表（Pivot Tables）')
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print('生成透视表')
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

'''
Pandas 为频率转换时重采样提供了虽然简单易用，但强大高效的功能，如，将秒级的数据转换为 5 分钟为频率的数据。这种操作常见于财务应用程序，
但又不仅限于此。详见时间序列 。
'''
print('\n')
print('时间序列')
rng = pd.date_range('1/1/2012', periods=100, freq='S')
print('rng')
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print('ts')
print(ts)
print('resample')
ts2 = ts.resample('5Min').sum()
print(ts2)

print('\n')
print('选择时区')
rng = pd.date_range('10/22/2020 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print('转换时区')
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.tz_convert('US/Eastern'))

print('\n')
print('类别型Categoricals')
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
# 将 grade 的原生数据转换为类别型数据：
df["grade"] = df["raw_grade"].astype("category")
print(df)
print('df[grade]')
print(df['grade'])
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df)
print('按类列分组（groupby）时，即便某类别为空，也会显示')
print(df.groupby('grade').size())


print('\n')
print('数据输入输出')
print('csv')
df.to_csv('foo.csv')
csvfile = pd.read_csv('foo.csv')
print(csvfile)

print('\n')
print('excel')
df.to_excel('foo.xlsx', 'sheet1')
excel = pd.read_excel('foo.xlsx')
print(excel)