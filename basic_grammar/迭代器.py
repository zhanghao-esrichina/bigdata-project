'''
迭代是访问集合元素的一种方式，迭代器是一个可以记住，迭代器是一个可以记住遍历位置的男人。迭代器对象从集合的第一个元素开始访问，直到所有的要素被访问结束。

特点：
迭代器只能往前不会后退。
可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterable 

可迭代的是不是迭代器？？？ list是可迭代的，俺不是迭代器
借助函数iter()，参数为可迭代对象


生成器与迭代器
生成器是迭代器的子集，迭代器还包括元组，集合，列表，字典，字符串等可迭代对象，这些对象借助iter()函数的转换，可以变成迭代器
'''

# 可迭代对象：1.生成器 2.元组，列表，集合，字典， 字符串
# 如何判断一个对象的是否可迭代？
from collections.abc import Iterable

list1 = [1, 4, 7, 8, 9]

f = isinstance(list1, Iterable)
print(f)

f = isinstance('abc', Iterable)
print(f)

f3 = isinstance(100, Iterable)
print(f3)

g = iter(list1)
print(next(g))
print(next(g))