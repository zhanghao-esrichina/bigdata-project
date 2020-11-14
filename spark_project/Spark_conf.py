# _*_ coding: utf-8 _*_
# 使用findspark初始化spark环境
import findspark
findspark.init()

# from pyspark.sql import SparkSession
# from pyspark.sql import functions
# from pyspark import SparkConf
# # 初始化
# spark = SparkSession.builder.master(
#     "local[*]").appName("FiratApp").getOrCreate()
#
#


from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

import os
os.environ['JAVA_HOME'] = r'C:\bigdata\Java\jdk1.8.0_171'


conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc = SparkContext(conf=conf)

sqlsc = SQLContext(sc)
# textfile = sc.textFile("../data/siweituxin.csv")
df = sqlsc.read.format('csv').option('delimiter', ',').option('header', 'true').load('./data/siweituxin.csv')
df.show(3)
