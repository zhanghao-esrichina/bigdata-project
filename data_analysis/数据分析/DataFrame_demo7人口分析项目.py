import numpy as np
import pandas as pd

abb = pd.read_csv("../课件/data/state-abbrevs.csv")
pop = pd.read_csv("../课件/data/state-population.csv")
area = pd.read_csv("../课件/data/state-areas.csv")
print(abb.head())
print(pop.head())

print('\n')
print('##### 将人口数据和各州数据进行合并')
abb_pop = pd.merge(
    abb,
    pop,
    left_on='abbreviation',
    right_on='state/region',
    how='outer')

print(abb_pop.head())

print('\n')
print('##### 将合并后的数据中重复的abbreviation列删除')
abb_pop.drop(labels='abbreviation', axis=1, inplace=True)
print(abb_pop.head())

print('\n')
print('##### 查看存在缺失数据的列，存在null')
print(abb_pop.isnull().any(axis=0))
print('\nabb.info可以通过查看记录数看出那及列有空值')
print(abb_pop.info())

print('##### 将state这一列中的空值对应的行数据取出')
# print(abb_pop['state'].isnull())
print(abb_pop.loc[abb_pop['state'].isnull()])