import os

# file = '/Users/zhanghao/code/py-workspace/basic_grammar/output.txt'

# print(os.path.isabs(file))

# filename = os.path.split(file)[1]
# print(filename[:filename.rfind('.')])


# print(os.path.splitext(file))
# print(os.path.getsize(file))
# print(os.path.join('', ''))


# print(os.path.dirname(file))
# print(os.getcwd())

# os.listdir() # 文件夹列表
# os.removedirs() # 
# os.mkdir() # 创建文件夹
# os.rmdir() # 删除空的文件夹
# os.remove() # 删除文件


# 复制文件
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)
        for file in filelist:
            path = os.path.join(src,file)
            with open(path,'rb') as rstream:
                container = rstream.read()

                path_target = os.path.join(target,file)
                with open(path_target, 'wb') as wstream:
                    wstream.write(container)
        else:
            print('复制完毕')


copy(r'/Users/zhanghao/code/py-workspace/basic_grammar/envParameter',r'/Users/zhanghao/code/py-workspace/basic_grammar/en')