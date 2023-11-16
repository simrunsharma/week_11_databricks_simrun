# # Databricks notebook source

# modern_file_namez_df[0].__getitem__('Year') + "-" + modern_file_namez_df[1].__getitem__('Year') 

# nintys_file_namez_df[0].__getitem__('Year') + "-" + nintys_file_namez_df[1].__getitem__('Year')

# nintys_df.write.format('parquet').mode('overwrite').save('/dbfs/nintys_df.parquet')

# display(dbutils.fs.ls("/dbfs/"))


# # COMMAND ----------