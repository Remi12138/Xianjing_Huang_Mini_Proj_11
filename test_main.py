import os
import pytest
from mylib.lib import (
    extract,
    load,
    describe,
    query,
    transform,
    start,
    end,
)


@pytest.fixture(scope="module")
def spark():
    spark = start("TestApp")
    yield spark
    end(spark)


def test_extract():
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load(spark):
    df = load(spark)
    assert df is not None
    assert df.count() > 0
    assert "country" in df.columns
    assert "total_litres_of_pure_alcohol" in df.columns


def test_describe(spark):
    df = load(spark)
    result = describe(df)
    assert result is None


def test_query(spark):
    df = load(spark)
    result = query(
        spark, df, "SELECT * FROM DrinkData WHERE country = 'Angola'", "DrinkData"
    )
    assert result is None


def test_transform(spark):
    df = load(spark)
    result = transform(df)
    assert result is None


if __name__ == "__main__":
    test_extract()
    test_load(spark)
    test_describe(spark)
    test_query(spark)
    test_transform(spark)
