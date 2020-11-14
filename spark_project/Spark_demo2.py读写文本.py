import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext,SparkConf

if __name__ == "__main__":
    sc = SparkContext('local', 'outliers')
    sqlsc = SQLContext(sc)
    # textfile = sc.textFile("../data/siweituxin.csv")
    df = sqlsc.read.format('csv').option('delimiter',',').option('header','true').load(r'C:\Users\zh\Desktop\pythonScript\PycharmProjects\spark\data\yellow_tripdata_2020-01.csv')
    df.show(3)
