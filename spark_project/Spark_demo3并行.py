import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


def add1(a, b):

    print("*"*55)
    print(a)
    print(b)
    return a + b+100

def remove_outliers(nums):
    stats = nums.stats()
    stddev = stats.stdev()
    return nums.filter(lambda x: abs(x - stats.mean()) < 3 * stddev)


if __name__ == '__main__':
    sc = SparkContext('local', 'outliers')

    # demo1
    # nums = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000])
    # output = sorted(remove_outliers(nums).collect())
    # print(output)

    # demo2
    rdd = sc.parallelize([('a', 1), ('b', 100), ('a', 300), ('b', 3), ('a', 200)])
    a = sorted(rdd.reduceByKey(add1).collect())
    print(a)
