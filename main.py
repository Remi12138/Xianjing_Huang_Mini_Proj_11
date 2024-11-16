from mylib.lib import (
    extract,
    load,
    describe,
    query,
    transform,
    start,
    end,
)


def main():
    # Extract
    extract()
    spark = start("DrinkConsumption")
    # Load
    df = load(spark)
    describe(df)
    # Query: Top 5 countries with the highest total litres of pure alcohol
    query(
        spark,
        df,
        """
        SELECT country, total_litres_of_pure_alcohol
        FROM DrinkData
        ORDER BY total_litres_of_pure_alcohol
        DESC
        LIMIT 5
        """,
        "DrinkData",
    )
    # Transformation
    transform(df)
    end(spark)


if __name__ == "__main__":
    main()
