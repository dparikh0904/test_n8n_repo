```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Movie Data Transformation") \
    .getOrCreate()

# Load the JSON data into a DataFrame (specify the path of the JSON file)
json_file_path = "path/to/movies.json"  # Update with the actual path
movies_df = spark.read.json(json_file_path)

# Display the initial schema of the DataFrame
movies_df.printSchema()

# Transform the data
transformed_df = movies_df.select(
    col("id"),
    col("title"),
    explode(col("genres")).alias("genre"),
    col("revenue"),
    to_date(col("release_date")).alias("release_date")
).filter(col("revenue").isNotNull() & (col("revenue") > 0))  # Filter out entries without revenue

# Display the schema of the transformed DataFrame
transformed_df.printSchema()

# Show some records from the transformed DataFrame
transformed_df.show(truncate=False)

# Write the transformed DataFrame to a new JSON file (specify the output path)
output_file_path = "path/to/transformed_movies.json"  # Update with the desired output path
transformed_df.write.json(output_file_path, mode='overwrite')

# Stop the Spark session
spark.stop()
```

Please ensure to replace `"path/to/movies.json"` and `"path/to/transformed_movies.json"` with the actual paths where your input JSON file is located and where you want the output file to be saved, respectively.