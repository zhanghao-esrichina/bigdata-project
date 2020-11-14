import numpy as np

'''
numpy.char.add()

numpy.char.add() 函数依次对两个数组的元素进行字符串连接。
'''
print('=====连接两个字符串')
print(np.char.add(['hello'], ['xyz']))
print('连接示例：')
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))

'''
numpy.char.multiply()

numpy.char.multiply() 函数执行多重连接。
'''
print('\n')
print('=====执行多重连接')
print(np.char.multiply('hello ', 3))

'''

numpy.char.center()

numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充。
'''
print('\n')
print('=====将字符串居中')
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('hello', 30, fillchar='*'))

'''
numpy.char.capitalize()
numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：

numpy.char.title()
numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写：

numpy.char.lower()
numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower。

numpy.char.upper()
numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper。
'''
print('\n')
print('=====将字符串的每个单词首字符大写')
print(np.char.capitalize('i like apple'))
print(np.char.title('i like apple'))
print(np.char.lower('I LIKE APPLE'))
print(np.char.upper('i like apple'))


'''
numpy.char.split()
numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。

numpy.char.splitlines()
numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。
'''
print('\n')
print('split 过指定分隔符对字符串进行分割')
print(np.char.split('i like apple'))
print(np.char.split('www.google.com', sep='.'))

# \n，\r，\r\n 都可用作换行符。
print(np.char.splitlines('i\nlike apple'))
print(np.char.splitlines('i\rlike \napple'))

'''
numpy.char.strip()
numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
'''
print('\n')
print('strip() 函数用于移除开头或结尾处的特定字符。')
print(np.char.strip('i like apple', 'e'))
# 移除数组元素头尾的 a 字符
print(np.char.strip(['i', 'like', 'apple'], 'e'))


'''
numpy.char.join()
numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
'''
print('\n')
print('join() 函数通过指定分隔符来连接数组中的元素或字符串')
print(np.char.join(',', ['apple', 'apple']))

# 指定多个分隔符操作数组元素
print(np.char.join([':', '-'], ['baidu', 'google']))

'''
numpy.char.replace()
numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
'''
print('\n')
print('replace() 函数使用新字符串替换字符串中的所有子字符串')
print(np.char.replace('i like apple', 'like', 'love'))

'''
numpy.char.encode()
numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。

numpy.char.decode()
numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
'''
print('\n')
print('encode 对数组的每个元素编码')
a = np.char.encode('apple', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))
