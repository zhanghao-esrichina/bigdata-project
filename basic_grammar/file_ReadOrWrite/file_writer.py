import os

filename = '/Users/zhanghao/code/py-workspace/file_ReadOrWrite/pi_digits2.txt'

# if not os.path.exists(filename):
    # os.mkfifo(filename)

with open(filename, 'w+') as file_object:
    file_object.write('i am zhanghao')

with open(filename,'a') as file_object2:
    file_object2.write('    superman')