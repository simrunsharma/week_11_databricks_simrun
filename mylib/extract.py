"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well

Jeopardy dataset
"""
import requests
from pyspark.sql import DataFrame


def extract(url:str):
  filename = url.split('/')[-1]
  with requests.get('https://datahub.io/core/glacier-mass-balance/r/glaciers.csv', stream=True) as r:
    with open("/dbfs/glaciers.csv", 'wb') as f:
      f.write(r.content)
  return filename

file_name = extract('https://datahub.io/core/glacier-mass-balance/r/glaciers.csv')

df = spark.read.format("csv").option("header","true").load("file:/dbfs/glaciers.csv")

display(df)

df = spark.read.format("csv").option("header","true").load("file:/dbfs/glaciers.csv")


# COMMAND ----------