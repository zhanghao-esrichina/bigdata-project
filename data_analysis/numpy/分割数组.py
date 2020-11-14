import numpy as np

'''
分割数组
函数 	数组及操作
split 	将一个数组分割为多个子数组
hsplit 	将一个数组水平分割为多个子数组（按列）
vsplit 	将一个数组垂直分割为多个子数组（按行）
numpy.split

numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：

numpy.split(ary, indices_or_sections, axis)

参数说明：

    ary：被分割的数组
    indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
    axis：沿着哪个维度进行切向，默认为0，横向切分。为1时，纵向切分

'''
a = np.arange(9)

print('第一个数组：')
print(a)
print('\n')

print('将数组分为三个大小相等的子数组：')
b = np.split(a, 3)
print(b)
print(np.array(b))
print('\n')

print('将数组在一维数组中表明的位置分割：')
b = np.split(a, [4, 7])
print(b)


'''
numpy.hsplit

numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
'''
print('\n')
print('numpy.hsplit 函数用于水平分割数组')
harr = np.floor(10 * np.random.random((2, 6)))
print('原array：')
print(harr)

print('拆分后：')
harr2 = np.hsplit(harr, 3)
print(harr2)
print(np.array(harr2))


'''
numpy.vsplit

numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。
'''
print('\n')
print('numpy.vsplit 沿着垂直轴分割')
a = np.arange(16).reshape(4, 4)

print('第一个数组：')
print(a)
print('\n')

print('竖直分割：')
b = np.vsplit(a, 2)
print(b)
print(np.array(b))
