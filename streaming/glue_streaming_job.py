from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, TimestampType

# Create Spark session for Glue
spark = SparkSession.builder.appName("RealTimeStreamingJob").getOrCreate()

# Define event schema
event_schema = StructType() \
    .add("event_id", StringType()) \
    .add("user_id", StringType()) \
    .add("event_type", StringType()) \
    .add("event_time", TimestampType())

# Read streaming data from Amazon Kinesis
raw_stream = spark.readStream \
    .format("kinesis") \
    .option("streamName", "event-stream") \
    .option("region", "us-east-1") \
    .option("startingposition", "latest") \
    .load()

# Parse JSON payload
parsed_stream = raw_stream.select(
    from_json(col("data").cast("string"), event_schema).alias("event")
).select("event.*")

# Write curated data to Amazon S3
query = parsed_stream.writeStream \
    .format("parquet") \
    .option("path", "s3://curated-zone/events/") \
    .option("checkpointLocation", "s3://checkpoints/events/") \
    .outputMode("append") \
    .start()

query.awaitTermination()
