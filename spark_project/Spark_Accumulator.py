import findspark
findspark.init()
from pyspark import SparkContext

def f(x):
    global num
    num += x


sc = SparkContext('local', 'Accumulator app')
num = sc.accumulator(10)


rdd = sc.parallelize([10, 30, 40, 50])
rdd.foreach(f)
final = num.value

print("Accumulated value is -> %i" % (final))
