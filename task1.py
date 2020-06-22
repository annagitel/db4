from pyspark import SparkConf, SparkContext

data = ["1 2 3 4 5 6 7 8 9 10 1 2 3 4 1 2 3"]
conf = SparkConf().setMaster("local[*]")
sc = SparkContext(conf=conf)
text_file = sc.parallelize(data)