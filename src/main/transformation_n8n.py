```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load JSON data into a DataFrame (update the path to your JSON file)
json_file_path = "path/to/movies.json"  # Update with the actual path to your JSON file
movies_df = spark.read.json(json_file_path)

# Display the initial DataFrame schema
movies_df.printSchema()

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Flatten the genres array
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out movies without revenue

# Show the schema of the transformed DataFrame
transformed_df.printSchema()

# Show the first few rows of the transformed DataFrame
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (update the output path as needed)
output_file_path = "path/to/transformed_movies.json"  # Update with the desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Make sure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with the actual paths for your input and output files, respectively.