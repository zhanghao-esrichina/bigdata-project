import pandas as pd
import numpy as np

'''
构建Series：
list，字典

Series常用方法：
head
tail
unique
isnull,notnull
add,sub,mull,mul,div
'''
s = pd.Series(data=np.random.randint(60, 100, size=(10,)))
# print(s.head())
# print(s.tail(5))
print(s.unique())
print(s)

print('Series的算术运算')
'''
Series算术运算法则：
索引一致的元素进行算术运算，否则补空
'''
s1 = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series(data=[1, 2, 3], index=['a', 'd', 'c'])
print(s1 + s2)
print()


print('测试Series构建')
dic = {'name': ['zhangsan', 'lisi']}
s3 = pd.Series(data=dic)
print(s3)
