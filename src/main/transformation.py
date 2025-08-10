```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, to_date

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MovieDataTransformation") \
    .getOrCreate()

# Sample nested JSON data (this would typically come from a file or another data source)
movie_json_data = '''
[
  {"title": "Movie A", "genres": ["Action", "Adventure"], "id": 1, "revenue": 1000000, "release_date": "2021-01-15"},
  {"title": "Movie B", "genres": ["Comedy"], "id": 2, "revenue": 500000, "release_date": "2021-02-20"},
  {"title": "Movie C", "genres": ["Drama", "Thriller"], "id": 3, "revenue": 2000000, "release_date": "2021-03-05"}
]
'''

# Read JSON data into DataFrame
df = spark.read.json(spark.sparkContext.parallelize([movie_json_data]))

# Transform the DataFrame: explode genres and convert release_date to date format
transformed_df = df.select(
    col("id"),
    col("title"),
    col("revenue"),
    to_date(col("release_date")).alias("release_date"),
    explode(col("genres")).alias("genre")
)

# Show the transformed DataFrame
transformed_df.show(truncate=False)

# Stop the Spark session
spark.stop()
```