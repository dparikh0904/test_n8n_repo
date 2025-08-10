```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date, date_format

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Read the JSON file
df = spark.read.json("path/to/movies.json")

# Display the original schema
df.printSchema()

# Explode the genres array column into multiple rows
df_exploded = df.withColumn("genre", explode(col("genres")))

# Select relevant columns and rename them
transformed_df = df_exploded.select(
    col("id").alias("movie_id"),
    col("title").alias("movie_title"),
    col("genre").alias("movie_genre"),
    col("revenue").alias("movie_revenue"),
    to_date(col("release_date")).alias("movie_release_date")
)

# Format the release date to 'yyyy-MM-dd' format
final_df = transformed_df.withColumn(
    "formatted_release_date",
    date_format(col("movie_release_date"), "yyyy-MM-dd")
).drop("movie_release_date")

# Show the transformed DataFrame
final_df.show(truncate=False)

# Write the transformed DataFrame to Parquet format
final_df.write.parquet("path/to/transformed_movies.parquet", mode="overwrite")

# Stop the Spark Session
spark.stop()
``` 

Make sure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.parquet"` with the actual paths to your input and output data.