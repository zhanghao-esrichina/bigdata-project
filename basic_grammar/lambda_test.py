# 匿名函数


from typing import List


def f1(a, b): return a + b


print(f1(1, 2))


list1 = [1, 3, 4, 5, 6]
m1 = map(lambda x: x * 2, list1)
print([i for i in m1])


print('===========result=================')
# 三元运算符
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))


print("\n")
print("匿名函数应用，filter()，sort()等，作为参数传入上列函数中")

students = [{'name': 'tom', 'age': 20}, {'name': 'jack', 'age': 15}, {
    'name': 'kone', 'age': 33}, {'name': 'peter', 'age': 18}]
result2 = filter(lambda x: x['age'] > 18, students)
print(list(result2))

students2 = sorted(students, key=lambda x: x['age'], reverse=True)
print(students2)
