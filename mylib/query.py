"""
query function
"""

from pyspark.sql import SparkSession


def query():
    """
    1. Classifies countries based on their total_litres_of_pure_alcohol 
    into three categories:
        High: More than 10 liters of alcohol per year.
        Moderate: Between 5 and 10 liters.
        Low: 5 liters or less.
    2. Adds a new column -- consumption_category.
    3. Orders data: By total_litres_of_pure_alcohol, so the booziest 
    countries are right at the top.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = """
        SELECT 
            country,
            beer_servings,
            spirit_servings,
            wine_servings,
            total_litres_of_pure_alcohol,
            CASE
                WHEN total_litres_of_pure_alcohol > 10 THEN 'High'
                WHEN total_litres_of_pure_alcohol > 5 THEN 'Moderate'
                ELSE 'Low'
            END AS consumption_category
        FROM alcohol_data
        ORDER BY total_litres_of_pure_alcohol DESC
    """
    query_result = spark.sql(query)
    return query_result



if __name__ == "__main__":
    query()