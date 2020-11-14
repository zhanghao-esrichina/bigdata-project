# 如果没有添加__all__，所有的都可以访问，如果添加上__all__=['','']列表中可以访问的
__all__ = ['models']

# 当导入包的时候，默认调用__init__.py文件
# 作用：
# 1.当导入包的时候，把一些初始化的函数、变量、类定义在__init__.py文件中
# 2.此文件中函数、变量等的访问，只需要通过包名、函数。。。
# 3.结合__all__=['','']，用于标示通过*可以访问的模块

print('article __init__...')


def  create_app(parameter_list):
    print('create app')

def printA(parameter_list):
    print('print A')