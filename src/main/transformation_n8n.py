```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Create a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON movie data into a DataFrame (adjust the path accordingly)
json_file_path = "path/to/movies.json"  # Update this path with the actual JSON file location
movies_df = spark.read.json(json_file_path)

# Display the initial schema of the DataFrame
movies_df.printSchema()

# Transform the dataset
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),  # Flatten the genres array
    col("revenue"),
    to_date(col("release_date")).alias("release_date")  # Convert release_date to DateType
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out rows with null or non-positive revenue

# Display the schema of the transformed DataFrame
transformed_df.printSchema()

# Show the transformed data
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (adjust the output path as necessary)
output_file_path = "path/to/transformed_movies.json"  # Update this path as needed
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Please ensure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with your actual file paths for input and output respectively.