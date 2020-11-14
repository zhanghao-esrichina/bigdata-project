import numpy as np

'''
NumPy 包含大量的各种数学运算的函数，包括三角函数，算术运算的函数，复数处理函数等。
'''

'''

三角函数：sin()、cos()、tan()。
'''

a = np.array([0, 30, 45, 60, 90])
print('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(a * np.pi / 180))
print('数组中角度的余弦值：')
print(np.cos(a * np.pi / 180))
print('数组中角度的正切值：')
print(np.tan(a * np.pi / 180))

'''
numpy.around() 函数返回指定数字的四舍五入值。

numpy.around(a,decimals)
参数说明：

    a: 数组
    decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置

'''

print('\n')
print('decimals: 舍入的小数位数。')
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print('原数组：')
print(a)
print('舍入后：')
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))


'''
numpy.floor()
numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整。

numpy.ceil()
numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。 
'''
print('\n')
print('floor() 返回小于或者等于指定表达式的最大整数，即向下取整。')
a = np.array([-1.7,1.5,-0.2,0.6,10])
print('提供的数组：')
print(a)
print('修改后的数组：')
print(np.floor(a))
print('ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。 ')
print(np.ceil(a))

