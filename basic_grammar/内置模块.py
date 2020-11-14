import sys
import time
import datetime
import random
import chardet
import string


print('------sys--------')
print(sys.version)
print(sys.argv)  # 接收命令行参数🐝🐝🐝


print('------time--------')
t = time.time()
print(time.ctime(t))
print(time.localtime(t))  # 将时间转为元组

t2 = time.localtime(t)
print(time.mktime(t2))  # 将元组转为时间

print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 将元组的时间转成字符串
print(time.strptime('2020/09/01', '%Y/%m/%d'))  # 将字符串转成元组的方式


print('------datetime--------')
print(datetime.timedelta(hours=2))
print(datetime.datetime.now().date())

print('------random--------')
print(random.random()) # random()返回0-1之间的随机小数
print(random.randrange(1,10))

# print('------ord--------')
# print(char(65))
# print(ord('A'))
# # print(ord('下')）

# print(char19989)

print('------hashlib--------')
import hashlib
msg= '中午一起去吃饭吧'
md5 = hashlib.md5(msg.encode('utf-8')) 

print(md5.hexdigest())