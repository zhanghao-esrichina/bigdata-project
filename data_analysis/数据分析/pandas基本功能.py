import pandas as pd
import numpy as np

# 重建索引
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas',
                                      'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

# 丢弃指定轴上的项
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop(['c'])
print(new_obj)
# 设置按照axis=1或者axis='columns'删除列的值
print('\n')
print("设置按照axis=1或者axis='columns'删除列的值")
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.sum(axis=0))
print(data.drop('Ohio', axis=0))

print(data.drop('two', axis=1))
print(data.drop('three', axis='columns'))


'''
对于DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc。它们可以让你用类似NumPy的标记，使用轴标签（loc）或整数索引（iloc），从DataFrame选择行和列的子集。
'''
print('\n')
print('特殊的标签运算符loc和iloc')
print(data)
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])

print('\n')
print('对于DataFrame，对齐操作会同时发生在行和列上')
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
print('把它们相加后将会返回一个新的DataFrame，其索引和列为原来那两个DataFrame的并集：')
'''
如果DataFrame对象相加，没有共用的列或行标签，结果都会是空：
'''
print(df1 + df2)


print('\n')
print('==========排序')
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print('Sort Series')
print(obj.sort_index())
print(obj.sort_values(ascending=False))
print('Sort DataFrame')
frame = pd.DataFrame(np.arange(12).reshape((3, 4)),
                     index=['three', 'one', 'four'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
print('在排序时，任何缺失值默认都会被放到Series的末尾')
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())


