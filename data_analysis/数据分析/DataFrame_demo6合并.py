import numpy as np
import pandas as pd

'''
合并
merge和concat区别自在于merge需要依赖某一共同列来进行合并
使用pd.merge合并时，会自动根据两者相同columbs名称的那一列作为key进行合并
注意每一列元素的顺序不要求一致

'''

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa'], 'group': [
                   'Accounting', 'Engineering', 'Engineering']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'zhnghao'], 'hire_date': [
    2004, 2008, 2012, 2015]})
print(df1)
print(df2)
print('\nmerge')
print(pd.merge(df1, df2, on='employee'))
'''
how 默认时内连接，设置为outer则为外连接，保留所有数据，还有left right
'''
print('\nhow=outer')
print(pd.merge(df1, df2, how='outer', on='employee'))
