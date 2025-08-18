```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON movie data into a DataFrame (make sure to update the file path)
json_file_path = "path/to/movies.json"  # Update with the path to your JSON file
movies_df = spark.read.json(json_file_path)

# Show the initial schema and a sample of the data
movies_df.printSchema()
movies_df.show(truncate=False)

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Flatten the genres array into rows
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out rows with null or non-positive revenue

# Show the transformed schema and a sample of the transformed data
transformed_df.printSchema()
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (make sure to update the output path)
output_file_path = "path/to/transformed_movies.json"  # Update with your output file path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to update the file paths specified in `json_file_path` and `output_file_path` with the actual paths to your input JSON file and desired output location, respectively.