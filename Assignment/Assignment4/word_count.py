from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col
import sys

# 创建 SparkSession 使用 vm1 的私有 IP 地址作为 Spark Master
spark = SparkSession.builder \
    .appName("WordCount") \
    .master("spark://172.31.1.153:7077") \  
    .getOrCreate()

# 从 HDFS 读取输入文件
input_path = sys.argv[1]
output_path = sys.argv[2]
df = spark.read.text(input_path)

# 统计单词出现次数
words = df.select(explode(split(col("value"), " ")).alias("word"))
word_counts = words.groupBy("word").count()

# 将结果保存为 CSV 格式到 HDFS
word_counts.write.csv(output_path)

# 停止 SparkSession
spark.stop()
