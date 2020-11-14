print('============推导式==============')
# 列表推导式
list1 = [1, 2, 1, 3, 5, 2, 1]

list2 = [x+1 for x in list1]
list3 = [x for x in list1 if x > 1]
print(list2)
print(list3)

newlist1 = [(x, y) for x in range(5) if x %
            2 == 0 for y in range(10) if y % 2 != 0]  # 前后两个for循环为嵌套关系
print(newlist1)

list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist2 = [i[-1] for i in list4]
print(newlist2)

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}
list5 = [dict1, dict2, dict3, dict4]
newlist3 = [employee['salary']+200 if employee['salary'] >
            5000 else employee['salary']+500 for employee in list5]
print(newlist3)
# 集合推导式，相对于列表推导式，区别在于集合推导式可以去重
set1 = {x+1 for x in list1}
set2 = {x for x in list1 if x > 1}

print(set1)
print(set2)


# 字典推导式
dict5 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
newdict1 = {value: key for key, value in dict5.items()}
print(newdict1)
