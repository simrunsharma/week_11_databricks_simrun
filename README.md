# Databricks End to End ETL Pipeline:
[![CI](https://github.com/simrunsharma/Individual_Project_3/actions/workflows/cicd.yml/badge.svg)](https://github.com/simrunsharma/Individual_Project_3/actions/workflows/cicd.yml)

## Dataset:
Average cumulative mass balance of “reference” Glaciers worldwide from 1945-2014 sourced from US EPA and the World Glacier Monitoring Service (WGMS). This is cumulative change in mass balance of a set of “reference” glaciers worldwide beginning in 1945. The values represents the average of all the glaciers that were measured. Negative values indicate a net loss of ice and snow compared with the base year of 1945. For consistency, measurements are in meters of water equivalent, which represent changes in the average thickness of a glacier.

## ETL Process: 
1. Extract : The `extract` function in the ETL pipeline downloads the CSV file containing average cumulative mass balance data of "reference" glaciers worldwide from 1945-2014. The function retrieves this data from the specified URL, saves it to the Databricks File System (DBFS), and then reads it into a PySpark DataFrame for further processing in the ETL pipeline.

2. Transform: The `transform_data` function in the ETL process for glacier data filters the original DataFrame (`df`) into two subsets: 'nintys' representing data from the 1990s and 'modern' representing data from the 2000s onwards. These subsets are stored as temporary views for further analysis. The function then returns DataFrames (`nintys_df` and `modern_df`) corresponding to these filtered time periods, facilitating the extraction of relevant information for downstream processing in the ETL pipeline.

3. Load: The `load` function in the glacier ETL process reads glacier data from a CSV file located in the Databricks File System (DBFS). The function uses PySpark to read the CSV file, allowing for schema customization using a predefined structure. After loading the data into a DataFrame, it is displayed, and then saved as a table named 'glaciers' in Spark SQL for further analysis, providing a structured and queryable representation of the glacier dataset.

# Delta Lake Usage:
The ETL pipeline utilizes Delta Lake for data storage. The provided code defines and overwrites a Delta table named 'glaciers' with the specified schema, including columns for 'Year,' 'Meancumulativemassbalance,' and 'Numberofobservations.' This Delta table serves as a persistent and versioned storage solution, enabling efficient data management and querying capabilities for glacier-related information in a structured format.

<img width="714" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/9a17acd1-df20-4e26-822b-4968e2b6c184">

# Usage of Spark SQL: 
The following code is used to start a spark session and then use it to load the csv into a readable format and then saved in the dbfs storage in databricks. 

```sh
import requests
from pyspark.sql import DataFrame
```
```sh
df = spark.read.format("csv").option("header", "true").load("file:/dbfs/glaciers.csv")
```
```sh
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define the schema for the CSV file
schema = StructType(
    [
        StructField("Year", StringType(), True),
        StructField("Meancumulativemassbalance", StringType(), True),
        StructField("Numberofobservations", StringType(), True),
    ]
)

# Read the CSV file with the specified schema
df = (
    spark.read.format("csv")
    .option("header", "true")
    .schema(schema)
    .load("file:/dbfs/glaciers.csv")
)

# Show the contents of the DataFrame
display(df)
```
# Data Transformations:
<img width="344" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/44ef4ca3-14ed-4c3f-9c3f-e539b2389f67">
<img width="298" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/1f69a219-7397-4f46-b157-86930192aee5">
<img width="321" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/e85e4179-6416-407b-b383-f43383188eb5">
<img width="310" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/a1ee08f7-f899-49c6-814b-0c0f5ce811a8">
<img width="428" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/8d929f87-4ba5-4647-b22c-26b9890d622e">

# Data Visualization: 
The following is the Mean Cumulative Mass Balance for the glaciers in the dataset. This data is in ascending order detailing the increase of mass for each glacier. 


<img width="148" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/7dff955d-5329-4c92-a440-d96f9dfa836f">

# Actionable Data-Driven Recommendations

1. **Prioritize Mitigation Strategies:**
   Concentrate mitigation efforts on glaciers showing persistent negative 'Meancumulativemassbalance,' indicating sustained ice and snow loss. Allocate resources strategically based on the severity of mass balance trends.

2. **Temporal Strategy Planning:**
   Analyze temporal patterns by considering 'Year' data to identify periods of accelerated mass loss. Tailor conservation strategies to address specific temporal trends, allowing for more effective intervention.

3. **Enhance Data Collection in Critical Years:**
   Intensify data collection efforts during years with extreme changes in 'Meancumulativemassbalance.' This targeted approach ensures a more detailed understanding of factors contributing to significant fluctuations and supports informed decision-making.

# Automated Trigger:
<img width="462" alt="image" src="https://github.com/simrunsharma/Individual_Project_3/assets/141798228/a40689ac-b7b3-4525-804a-e2d17f64e7ce">
