import random as rd
import time


def test(fn, num):
    start_time = time.time()

    for i in range(num):
        rd.random()
        time.sleep(0.5)

        end_time = time.time()

        seconds = str(end_time - start_time)
        fn(i, seconds)


def test_callback(n, tm_s):
    print('生成{0}个数，用时{1}秒'.format(n, tm_s))
    # print('生成{0}个数，用时{1}秒')


test(test_callback, 10)
