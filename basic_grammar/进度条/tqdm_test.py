from tqdm import tqdm
import time

# 1.默认设置打印速度
# for i in tqdm(range(1000)):
#     time.sleep(0.01)


# 2.自定义格式
pbar = tqdm(['a', 'b', 'c', 'd'])
for char in pbar:
    time.sleep(0.5)
    pbar.set_description("processing {}".format(char))


# 3.按时间控制更新的进度
with tqdm(total=100) as target:
    for i in range(20):
        time.sleep(0.5)
        target.update(5)

# target = tqdm(total=100)
# for i in range(20):
#     time.sleep(0.5)
#     target.update(5)

# target.close()
