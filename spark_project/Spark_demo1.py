# _*_ coding: utf-8 _*_
# 使用findspark初始化spark环境
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark import SparkConf
# 初始化
spark = SparkSession.builder.master(
    "local[*]").appName("FiratApp").getOrCreate()

# 下面两句都可以获取0到9的数据
data = spark.createDataFrame(map(lambda x: (x,), range(10)), ["id"])
# data = spark.range(0, 10).select(col("id").cast("double"))


# 求和
data.agg({'id': 'sum'}).show()

# 关闭
spark.stop()
