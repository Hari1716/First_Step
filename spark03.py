import os
os.environ['SPARK_HOME'] = "C:\spark-3.5.3-bin-hadoop3"
os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'
os.environ['PYSPARK_PYTHON'] = 'python'

spark = SparkSession.builder \
    .appName("MySparkApplication") \
    .config("spark.executor.memory", "2g") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

spark

spark.stop()