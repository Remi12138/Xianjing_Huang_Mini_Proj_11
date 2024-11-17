import matplotlib.pyplot as plt
from pyspark.sql import SparkSession

def visualize(input_path):
    """
    Visualizes the saved query result by creating:
    1. A bar plot of the top 10 countries by total alcohol consumption.
    2. A stacked bar plot of beer, spirit, and wine servings for the top 10 countries.
    """
    spark = SparkSession.builder.appName("Visualize Data").getOrCreate()

    # Load the saved query result
    query_result = spark.read.parquet(input_path)
    df = query_result.toPandas()

    # Bar Plot: Top 10 countries by total_litres_of_pure_alcohol
    plt.figure(figsize=(12, 6))
    plt.bar(df['country'], df['total_litres_of_pure_alcohol'], color='skyblue')
    plt.title("Top 10 Countries by Total Alcohol Consumption")
    plt.xlabel("Country")
    plt.ylabel("Total Litres of Pure Alcohol")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top_10_countries.png")
    plt.show()

    # Stacked Bar Plot: Breakdown of alcohol servings by type
    plt.figure(figsize=(12, 6))
    plt.bar(
        df['country'], 
        df['beer_servings'], 
        label="Beer Servings", 
        color='gold'
    )
    plt.bar(
        df['country'], 
        df['spirit_servings'], 
        bottom=df['beer_servings'], 
        label="Spirit Servings", 
        color='silver'
    )
    plt.bar(
        df['country'], 
        df['wine_servings'], 
        bottom=df['beer_servings'] + df['spirit_servings'], 
        label="Wine Servings", 
        color='lightcoral'
    )
    plt.title("Breakdown of Alcohol Servings by Type")
    plt.xlabel("Country")
    plt.ylabel("Servings")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("alcohol_servings_breakdown.png")
    plt.show()


if __name__ == "__main__":
    input_path = "dbfs:/FileStore/mini_proj11/query_result.parquet"
    visualize(input_path)
