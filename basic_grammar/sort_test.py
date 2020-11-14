
presents = [{'name': 'Susan', 'age': 50}, {'name': 'Christopher', 'age': 47}]


def sortbyname(item):
    return item['name']


def sortbyage(item):
    return item['age']


# presents.sort(key=sortbyage)
# print(presents)


presents.sort(key=lambda item: item['name'])
print(presents)

presents.sort(key=lambda item: item['age'])
print(presents)

print()
presents.sort(key=lambda item: len(item['name']))
print(presents)
