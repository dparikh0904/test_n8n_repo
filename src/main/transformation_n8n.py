```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame
json_file_path = "path/to/movies.json"  # Update this path with your actual JSON file location
movies_df = spark.read.json(json_file_path)

# Show the initial DataFrame schema and a preview of the data
movies_df.printSchema()
movies_df.show(truncate=False)

# Transform the data
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Explode the genres array to separate rows
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies with no or negative revenue

# Show the schema and a few rows of the transformed DataFrame
transformed_df.printSchema()
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file
output_file_path = "path/to/transformed_movies.json"  # Update this path for the output file location
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Ensure to update the file paths in `json_file_path` and `output_file_path` to reflect the actual locations of your input and output files.