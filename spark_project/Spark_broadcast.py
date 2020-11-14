import findspark
findspark.init()

from pyspark import SparkContext

sc = SparkContext('local', 'broadcast app')
words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"])
data = words_new.value
print("Stored data -> %s" % (data))
element = words_new.value[2]
print("Printing a particular element in RDD -> %s" % (element))
