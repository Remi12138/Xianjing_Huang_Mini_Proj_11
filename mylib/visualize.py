"""
visualize function
"""

import matplotlib.pyplot as plt
from query import query


def visualize():
    query_result = query()
    df = query_result.toPandas()

    # Boxplot for different alcohol types
    plt.figure(figsize=(10, 6))
    df[["beer_servings", "spirit_servings", "wine_servings"]].boxplot()
    plt.title("Distribution of Alcohol Servings")
    plt.xlabel("Alcohol Type")
    plt.ylabel("Servings")
    plt.tight_layout()
    plt.savefig("alcohol_types.png")
    plt.show()

    # Bar chart for consumption categories
    category_counts = df["consumption_category"].value_counts()

    plt.figure(figsize=(8, 6))
    category_counts.plot(kind="bar", color="skyblue")
    plt.title("Number of Countries by Consumption Category")
    plt.xlabel("Consumption Category")
    plt.ylabel("Number of Countries")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("categories.png")
    plt.show()


if __name__ == "__main__":
    visualize()