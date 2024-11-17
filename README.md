# Xianjing_Huang_Mini_Proj_11
[![CI](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_11/actions/workflows/ci.yml/badge.svg)](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_11/actions/workflows/ci.yml)

### Directory Tree Structure
```
Xianjing_Huang_Mini_Proj_11/
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
│   ├── extract.py
│   ├── load.py
│   ├── query.py
│   └── visualize.py
├── .gitignore
├── alcohol_servings_breakdown.png
├── job.py
├── LINCENSE
├── main.py
├── Makefile
├── README.md
├── requirements.txt
├── setup.sh
├── test_main.py
└── top_10_countries.png
```
`.devcontainer`: config for a Python and PySpark environment.

`lib.py`: 
* `extract.py`: downloads a file from the specified URL and saves it to the specified DBFS path.
* `load.py`: loads data from a CSV file into a PySpark DataFrame and saves it as a table.
* `query.py`: runs an SQL query to select the top 10 countries by total alcohol consumption, saves the result to a Parquet file, and displays it.
* `visualize.py`: visualizes the saved query result by creating:
    1. a bar plot of the top 10 countries by total alcohol consumption.
    2. a stacked bar plot of beer, spirit, and wine servings for the top 10 countries.

`main.py`: perform extract, load, query, and visualize.

`job.py`: utilize the Databricks API to run a job on my Databricks workspace such that when a user pushes to this repo it will initiate a job run.

`test_main.py`: test if a file path exists and auth settings still work.

`Makefile`: defines scripts for common project tasks such as install, lint format, test, and job run.

`.github/workflows/ci.yml`: defines the GitHub Actions workflow for format, install, lint, test, and run databricks job.

`requirements.txt`: project dependencies.

### Requirements
* Create a data pipeline using Databricks
* Include at least one data source and one data sink

### Preparation
1. Create a Databricks workspace on Azure.
2. Connect Github account to Databricks Workspace.
3. Create global init script for cluster start to store enviornment variables.
4. Clone repo into Databricks workspace.
5. Create a Databricks cluster that supports Pyspark, link requirements.txt to Libraries.
6. Create a job on Databricks to build pipeline.
7. Extract task (Data Source): mylib/extract.py
8. Load Task: mylib/load.py
9. Query Task (Data Sink): mylib/query.py. The query result saved as a Parquet file.
10. Visualize Task (Data Sink): mylib/visualize.py. Visualization plots saved as PNG files: alcohol_servings_breakdown.png, top_10_countries.png

### Job Run from Automated Trigger
The workflow created in Databricks consists of 4 tasks: Extract, Load, Query and Visualize.
<img src="/imgs/004.png" alt="4" style="height:100px;">
![5](/imgs/005.png)
![6](/imgs/006.png)

### Install, check format and test errors
1. Install dependencies `make install`

   <img src="/imgs/000.png" alt="0" style="height:80px;">
2. Format code `make format`

   <img src="/imgs/001.png" alt="1" style="height:50px;">
3. Lint code `make lint`

   <img src="/imgs/002.png" alt="2" style="height:50px;">
4. Test code `make test`

   <img src="/imgs/003.png" alt="3" style="height:100px;">

### Data Extracting
![7](/imgs/007.png)

### Data Loading
![8](/imgs/008.png)

### Data Query
Run an SQL query to select the top 10 countries by total alcohol consumption, saves the result to a Parquet file, and displays it.
![9](/imgs/009.png)

### Visualization
![10](/alcohol_servings_breakdown.png)
![11](/top_10_countries.png)
