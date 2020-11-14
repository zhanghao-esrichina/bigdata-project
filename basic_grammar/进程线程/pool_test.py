

'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，但如果是上百个甚至上千个目标，手动的去创建
进程的工作量巨大，此时就可以用到Multiprocessor模块提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没满，那么就会创建一个新的进程用来执行该请求，但如果池中但
进程数已经达到指定的最大值，那么该请求就会等待，知道池中的进程结束，才会创建新的进程来执行。

非阻塞式进程, 全部添加到对列中，立刻返回，并没有等待其他到进程完毕,但是回调函数会等待


'''
# 1.不使用回调函数
from multiprocessing import Pool
import time
from random import random
import os
from typing import Container

container = []


def task(task_name):
    print('开始做任务：', task_name)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    # print('完成任务: {0},耗时：{1},进程id：{2}'.format(task_name, end-start, os.getpid()))
    print('完成任务: {0},耗时：{1},进程id：{2}'.format(
        task_name, end-start, os.getpid()))


# if __name__ == "__main__":
#     pool = Pool(4)

#     tasks = ['听音乐', '洗衣服', '读书', '打游戏', '散步', '看孩子']
#     for i in tasks:
#         pool.apply_async(task, args=(i,))
#     pool.close()  # 添加任务结束
#     pool.join()


# 2.使用回调函数
# from multiprocessing import Pool
# import time
# from random import random
# import os
# from typing import Container

# container = []


# def task(task_name):
#     print('开始做任务：', task_name)
#     start = time.time()
#     time.sleep(random()*2)
#     end = time.time()
#     # print('完成任务: {0},耗时：{1},进程id：{2}'.format(task_name, end-start, os.getpid()))
#     return '完成任务: {0},耗时：{1},进程id：{2}'.format(task_name, end-start, os.getpid())


# def callback_func(n):
#     container.append(n)


# if __name__ == "__main__":
#     pool = Pool(5)

#     tasks = ['听音乐', '洗衣服', '读书', '打游戏', '散步', '看孩子']
#     for i in tasks:
#         # pool.apply_async(task, args=(i,))  # 异步调用函数
#         pool.apply_async(task, args=(i,), callback=callback_func)
#     pool.close()  # 停止添加进程
#     pool.join()

#     for c in container:
#         print(c)
#     print('sucessful!!!!!!')

# 3.阻塞式
'''
添加一个任务执行一个，如果前一个任务没有完成后面一个任务无法执行
'''
if __name__ == "__main__":
    pool = Pool(5)
    tasks = ['听音乐', '洗衣服', '读书', '打游戏', '散步', '看孩子']
    for t in tasks:
        pool.apply(task, args=(t,))
        # pool.apply_async()

    print('sucessful')
