```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MovieDataTransformation") \
    .getOrCreate()

# Sample Input: Replace with your actual JSON file path
input_json_path = "path/to/movies.json"

# Load the JSON data
movies_df = spark.read.json(input_json_path)

# Inspect the schema (optional)
movies_df.printSchema()

# Transformations

# 1. Explode genres into separate rows
exploded_genres_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    col("release_date")
)

# 2. Parse release_date to a proper date format
final_df = exploded_genres_df.withColumn(
    "release_date",
    to_date(col("release_date"), "yyyy-MM-dd")  # Adjust the format if necessary
)

# Select the required columns
transformed_df = final_df.select(
    "id",
    "title",
    "genre",
    "revenue",
    "release_date"
)

# Show the result (optional)
transformed_df.show(truncate=False)

# Write to a new JSON file or any other destination
output_json_path = "path/to/transformed_movies.json"
transformed_df.write.json(output_json_path, mode="overwrite")

# Stop the Spark session
spark.stop()
```