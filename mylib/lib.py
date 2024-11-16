import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round
from pyspark.sql.types import StructType, StructField, StringType, FloatType

LOG_FILE = "output_data_log.md"

def log(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")

def start(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end(spark):
    spark.stop()
    return "stopped spark session"

def extract(url = 'https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/alcohol-consumption/drinks.csv',
            file_path="data/drinks.csv",
            directory="data"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if url:
        with requests.get(url) as r:
            with open(file_path, "wb") as f:
                f.write(r.content)
    return file_path

def load(spark, data="data/drinks.csv", name="DrinkData"):
    """load data"""
    # data preprocessing by setting schema
    schema = StructType([
        StructField("country", StringType(), True),
        StructField("beer_servings", FloatType(), True),
        StructField("spirit_servings", FloatType(), True),
        StructField("wine_servings", FloatType(), True),
        StructField("total_litres_of_pure_alcohol", FloatType(), True)
    ])
    df = spark.read.option("header", "true").schema(schema).csv(data)
    log("load data", df.limit(10).toPandas().to_markdown())
    return df

def query(spark, df, query, name):
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)
    log("query data", spark.sql(query).toPandas().to_markdown(), query)
    return spark.sql(query).show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log("describe data", summary_stats_str)
    return df.describe().show()


def transform(df):
    """Transform to add 'average_servings' and 'total_alcohol_servings' columns"""
    # Calculate total servings by summing beer, spirit, and wine servings
    df = df.withColumn(
        "total_alcohol_servings",
         col("beer_servings") + col("spirit_servings") + col("wine_servings"))

    # Calculate average servings
    df = df.withColumn(
        "average_servings",
         round((col("beer_servings")
                + col("spirit_servings")
                 + col("wine_servings")) / 3, 2))

    log("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()