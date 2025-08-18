```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame (update the file path as needed)
json_file_path = "path/to/movies.json"  # Update with the actual path to your JSON file
movies_df = spark.read.json(json_file_path)

# Display the initial DataFrame schema and a sample of the data
movies_df.printSchema()
movies_df.show(truncate=False)

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Flatten the genres array into separate rows
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies with no or non-positive revenue

# Show the schema and the transformed data
transformed_df.printSchema()
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (update the output path as needed)
output_file_path = "path/to/transformed_movies.json"  # Update with your desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to update `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with the actual paths for your input JSON file and desired output file location.