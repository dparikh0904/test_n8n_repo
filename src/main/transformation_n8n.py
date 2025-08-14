```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date, trim

# Create a Spark session
spark = SparkSession.builder \
    .appName("MovieDataTransformation") \
    .getOrCreate()

# Load the JSON data from the specified file path
input_json_path = "path/to/movies.json"  # Replace with your actual JSON file path
movies_df = spark.read.json(input_json_path)

# Transformations
# 1. Explode the 'genres' column to create a row for each genre
exploded_genres_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    col("release_date")
)

# 2. Convert 'release_date' to a proper date format
final_df = exploded_genres_df.withColumn(
    "release_date",
    to_date(col("release_date"), "yyyy-MM-dd")  # Adjust format if necessary
)

# 3. Trim whitespace from the 'genre' column for cleaner output
final_df = final_df.withColumn("genre", trim(col("genre")))

# Select the necessary columns in the desired order
transformed_df = final_df.select(
    "id",
    "title",
    "genre",
    "revenue",
    "release_date"
)

# Show the transformed DataFrame (optional)
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a JSON file
output_json_path = "path/to/transformed_movies.json"  # Specify the output path
transformed_df.write.json(output_json_path, mode="overwrite")

# Stop the Spark session
spark.stop()
```