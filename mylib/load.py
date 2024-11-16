"""
load function
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="dbfs:/FileStore/mini_proj11/drinks.csv"):
    spark = SparkSession.builder.appName("loadCSV").getOrCreate()
    # load csv and transform it by inferring schema 
    drinks_df = spark.read.csv(dataset, header=True, inferSchema=True)

    # add unique IDs to the DataFrames
    drinks_df = drinks_df.withColumn("id", monotonically_increasing_id())

    # transform into a delta lakes table and store it 
    drinks_df.write.format("delta").mode("overwrite").saveAsTable("drinks_delta")
    
    num_rows = drinks_df.count()
    print(num_rows)
    
    return "finished transform and load"

if __name__ == "__main__":
    load()