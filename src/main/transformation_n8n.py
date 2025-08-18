```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame (adjust the path as needed)
json_file_path = "path/to/movies.json"  # Update with the actual path
movies_df = spark.read.json(json_file_path)

# Display the initial DataFrame schema
movies_df.printSchema()

# Transform the data
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    to_date(col("release_date")).alias("release_date")
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies with no or negative revenue

# Display the schema of the transformed DataFrame
transformed_df.printSchema()

# Show some records from the transformed DataFrame
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (adjust the output path as needed)
output_file_path = "path/to/transformed_movies.json"  # Update with the desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to update the `json_file_path` and `output_file_path` with the correct paths for your JSON input file and desired output file location respectively.