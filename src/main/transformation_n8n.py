```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Read the JSON file
df = spark.read.json("path/to/movies.json")

# Display the original schema
df.printSchema()

# Explode the genres array into multiple rows
df_exploded = df.withColumn("genre", explode(col("genres")))

# Transform the DataFrame to select relevant fields
transformed_df = df_exploded.select(
    col("id").alias("movie_id"),
    col("title").alias("movie_title"),
    col("genre").alias("movie_genre"),
    col("revenue").alias("movie_revenue"),
    to_date(col("release_date")).alias("movie_release_date")
)

# Show the transformed DataFrame
transformed_df.show(truncate=False)

# Write the transformed DataFrame to Parquet format
transformed_df.write.parquet("path/to/transformed_movies.parquet", mode="overwrite")

# Stop the Spark Session
spark.stop()
```

Replace `"path/to/movies.json"` and `"path/to/transformed_movies.parquet"` with the appropriate file paths for your input JSON and desired output location.