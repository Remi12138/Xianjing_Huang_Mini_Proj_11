# Xianjing_Huang_Mini_Proj_11
[![CI](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_10/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_10/actions/workflows/ci.yml)

### Directory Tree Structure
```
Xianjing_Huang_Mini_Proj_10/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── drinks.csv
├── imgs/
├── mylib/
│   └── lib.py
├── .gitignore
├── main.py
├── Makefile
├── output_data_log.md
├── README.md
├── requirements.txt
├── setup.sh
└── test_main.py
```
`.devcontainer`: config for a Python and PySpark environment.

`lib.py`: 
* start a spark session via `start`
* end the spark session via `end`
* extract the dataset via `extract`
* load the dataset via `load`
* get descriptive statistics via `descibe`
* query the dataset via `query`
* transform to add 2 columns on the dataset via `transform`

`main.py`: use PySpark to perform data processing, include query and transformation.

`test_main.py`: test functions in main.

`Makefile`: defines scripts for common project tasks such as install, lint format, test, and 'generate and push report'.

`.github/workflows/ci.yml`: defines the GitHub Actions workflow for format, install, lint, test, and generate_and_push.

`requirements.txt`: project dependencies.

### Requirements
* Use PySpark to perform data processing on a large dataset
* Include at least one Spark SQL query and one data transformation

### Preparation
1. Open codespaces
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed
3. If running locally, `git clone` the repository and use `make install`
   ![0](/imgs/000.png)
4. run: `python3 main.py`

### Check format and test errors
1. Format code `make format`
   ![1](/imgs/001.png)
2. Lint code `make lint`
   ![2](/imgs/002.png)
3. Test code `make test`
   ![3](/imgs/003.png)

### Data Loading
The dataset records alcohol consumption in different countries.
Sample data structure:

|          country|beer_servings|spirit_servings|wine_servings|total_litres_of_pure_alcohol|
|-----------------|-------------|---------------|-------------|----------------------------|
|      Afghanistan|          0.0|            0.0|          0.0|                         0.0|
|          Albania|         89.0|          132.0|         54.0|                         4.9|
|          Algeria|         25.0|            0.0|         14.0|                         0.7|

### Data Description
After loading, basic statistics are generated to summarize the dataset.

|summary|    country|     beer_servings|  spirit_servings|    wine_servings|total_litres_of_pure_alcohol|
|-------|-----------|------------------|-----------------|-----------------|----------------------------|
|  count|        193|               193|              193|              193|                         193|
|   mean|       NULL|106.16062176165804|80.99481865284974|49.45077720207254|           4.717098425205198|
| stddev|       NULL| 101.1431025393134|88.28431210968618|79.69759845763012|          3.7732981308860754|
|    min|Afghanistan|               0.0|              0.0|              0.0|                         0.0|
|    max|   Zimbabwe|             376.0|            438.0|            370.0|                        14.4|


### Data Querying
Query data using spark sql.

Example query: Top 5 countries with the highest total litres of pure alcohol
```sql
  SELECT country, total_litres_of_pure_alcohol
  FROM DrinkData
  ORDER BY total_litres_of_pure_alcohol
  DESC
  LIMIT 5
```
|  country|total_litres_of_pure_alcohol|
|---------|----------------------------|
|  Belarus|                        14.4|
|Lithuania|                        12.9|
|  Andorra|                        12.4|
|  Grenada|                        11.9|
|   France|                        11.8|

### Data Transformation

The transformation step adds columns to the dataset, including:
- **total_alcohol_servings**: total servings of beer, spirit, and wine servings.
- **average_servings**: average servings of beer, spirit, and wine servings.

|          country|beer_servings|spirit_servings|wine_servings|total_litres_of_pure_alcohol|total_alcohol_servings|average_servings|
|-----------------|-------------|---------------|-------------|----------------------------|----------------------|----------------|
|      Afghanistan|          0.0|            0.0|          0.0|                         0.0|                   0.0|             0.0|
|          Albania|         89.0|          132.0|         54.0|                         4.9|                 275.0|           91.67|
|          Algeria|         25.0|            0.0|         14.0|                         0.7|                  39.0|            13.0|

### PySpark Log
Generate and push PySpark output log via CI/CD.
You can find it here [PySpark Log](/output_data_log.md).