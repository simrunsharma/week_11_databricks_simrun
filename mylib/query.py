'''
Transforms the data from the csv file into a dataframe. Then manipulates the data to get the desired output.
'''

%sql
select * from df_table

%sql
create or replace temp view nintys as select * from df_table where Year like '19%' order by Year asc;
create or replace temp view modern as select * from df_table where Year like '20%' order by Year asc;

nintys_df = spark.sql("select * from nintys")
modern_df = spark.sql("select * from modern")

def transform_data(df: DataFrame):
  spark.sql("create or replace temp view nintys as select * from df_table where Year like '19%' order by Year asc;")
  nintys_df = spark.sql("select * from nintys")
  spark.sql("create or replace temp view modern as select * from df_table where Year like '20%' order by Year asc;")
  modern_df = spark.sql("select * from modern")
  return nintys_df, modern_df

df.createOrReplaceTempView("df_table")
x, y = transform_data(df)

display(y)
display(x)

nintys_file_namez = spark.sql("(select * from nintys order by Year ASC limit 1) union (select * from nintys order by Year DESC limit 1)")
modern_file_namez = spark.sql("(select * from modern order by Year ASC limit 1) union (select * from modern order by Year DESC limit 1)")

display(nintys_file_namez)
display(modern_file_namez)

modern_file_namez_df = modern_file_namez.collect()
print(modern_file_namez_df)

nintys_file_namez_df = nintys_file_namez.collect()
print(nintys_file_namez_df)

# COMMAND ----------