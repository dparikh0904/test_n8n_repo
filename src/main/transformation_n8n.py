```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Path to the JSON file (update this path as needed)
json_file_path = "path/to/movies.json"

# Read the JSON data into a DataFrame
movies_df = spark.read.json(json_file_path)

# Show the initial DataFrame schema
movies_df.printSchema()

# Transformations
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    to_date(col("release_date")).alias("release_date")
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies with no revenue

# Show the transformed DataFrame schema
transformed_df.printSchema()

# Show the first few rows of the transformed DataFrame
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (update this path as needed)
output_file_path = "path/to/transformed_movies.json"
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to update the `json_file_path` and `output_file_path` with the actual paths where your input JSON file is located and where you want to save the output, respectively.