from matplotlib import pyplot as plt
import numpy as np
import matplotlib

'''
Matplotlib 是 Python 的绘图库。 它可与 NumPy 一起使用，提供了一种有效的 MatLab 开源替代方案。 它也可以和图形工具包一起使用，如 PyQt 和 wxPython。

pip3 安装：

pip3 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()

# x = np.arange(1, 11)
# y=np.sin(x*np.pi/180)
# # y = np.sin(x * np.pi / 180))
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()


# print('matplotlib 生成正弦波图。')
# import numpy as np
# import matplotlib.pyplot as plt
# # 计算正弦曲线上点的 x 和 y 坐标
# x = np.arange(0,  3  * np.pi,  0.1)
# y = np.sin(x)
# plt.title("sine wave form")
# # 使用 matplotlib 来绘制点
# plt.plot(x, y)
# plt.show()


'''
bar()

pyplot 子模块提供 bar() 函数来生成条形图。
'''

x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
