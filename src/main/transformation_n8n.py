```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame
json_file_path = "path/to/movies.json"  # Update with the actual path to your JSON file
movies_df = spark.read.json(json_file_path)

# Display the initial DataFrame schema
movies_df.printSchema()

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Flatten the genres array to individual rows
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out items with no revenue

# Show the schema of the transformed DataFrame
transformed_df.printSchema()

# Show the transformed data
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file
output_file_path = "path/to/transformed_movies.json"  # Update with the desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Please ensure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with the actual paths for your input JSON file and desired output file location, respectively.