from pyspark.sql import SparkSession

def load(file_path):
    """
    Loads data from a CSV file into a PySpark DataFrame and saves it as a table.
    """
    spark = SparkSession.builder.appName("Load Data").getOrCreate()
    print(f"Loading data from {file_path} into a Spark DataFrame...")
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    print(f"Data successfully loaded into a DataFrame with {df.count()} rows.")

    # Persist the DataFrame as a table
    df.write.format("delta").mode("overwrite").saveAsTable("alcohol_data")
    print("Data saved as a Delta table: alcohol_data")


if __name__ == "__main__":
    file_path = "dbfs:/FileStore/mini_proj11/drinks.csv"
    load(file_path)
