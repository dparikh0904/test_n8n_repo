```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame (update the path with your actual JSON file location)
json_file_path = "path/to/movies.json"  # Update this path with the path to your JSON file
movies_df = spark.read.json(json_file_path)

# Show the initial schema of the DataFrame
movies_df.printSchema()

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Explode the genres array
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies with no or negative revenue

# Show the schema and a few records of the transformed DataFrame
transformed_df.printSchema()
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (update the output path as needed)
output_file_path = "path/to/transformed_movies.json"  # Update with your desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with the actual file paths to your input and output locations.