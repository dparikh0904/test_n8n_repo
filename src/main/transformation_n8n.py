```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date, trim

# Create a Spark session
spark = SparkSession.builder \
    .appName("MovieDataTransformation") \
    .getOrCreate()

# Load the JSON data from the specified path
input_json_path = "path/to/movies.json"  # Replace with your actual JSON file path
movies_df = spark.read.json(input_json_path)

# Inspect the schema of the input DataFrame (optional)
movies_df.printSchema()

# Transformations
# 1. Explode the 'genres' column to create a row for each genre
exploded_genres_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    col("release_date")
)

# 2. Parse 'release_date' to a DateType
final_df = exploded_genres_df.withColumn(
    "release_date",
    to_date(col("release_date"), "yyyy-MM-dd")  # Adjust date format if necessary
)

# 3. Trim white spaces from the genre column
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
output_json_path = "path/to/transformed_movies.json"  # Replace with your desired output path
transformed_df.write.json(output_json_path, mode="overwrite")

# Stop the Spark session
spark.stop()
```