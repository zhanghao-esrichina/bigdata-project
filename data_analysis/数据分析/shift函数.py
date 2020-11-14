
'''
shift函数是对数据进行移动的操作，假如现在有一个DataFrame数据df，如下所示：
index	value1
A	0
B	1
C	2
D	3
那么如果执行以下代码：

df.shift()
就会变成如下：
index	value1
A	NaN
B	0
C	1
D	2
看一下函数原型：

DataFrame.shift(periods=1, freq=None, axis=0)
参数
periods：类型为int，表示移动的幅度，可以是正数，也可以是负数，默认值是1,1就表示移动一次，注意这里移动的都是数据，而索引是不移动的，移动之后没有对应值的，就赋值为NaN。
执行以下代码：

'''

import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(0, 10, size=(2, 3)))
print(df)
print(df.shift(1))
print(df[1].shift(1))
