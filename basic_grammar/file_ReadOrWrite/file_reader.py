# with open('file/pi_digits.txt') as file_object:
#     contents=file_object.read()
#     print(contents)

filename = '/Users/zhanghao/code/py-workspace/file_ReadOrWrite/pi_digits.txt'
#read row by row
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('--------------------------')
with open(filename) as file_object2:
    lines=file_object2.readlines()
    print(lines)

    

