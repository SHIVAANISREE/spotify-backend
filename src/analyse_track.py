from pyspark.sql import SparkSession

def analyze_top_tracks(csv_file_path, top_n=99999):
    # Create Spark session
    spark = SparkSession.builder \
        .appName("Spotify Track Analytics") \
        .getOrCreate()

    # Load CSV into DataFrame
    df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

    # Sort by Popularity (descending)
    top_tracks = df.orderBy(df["Popularity"].desc())

    # Show top N tracks
    print(f"\n🎧 Top {top_n} Most Popular Tracks:\n")
    result = top_tracks.select("Track Name", "Album", "Popularity","Spotify URL", "Duration (min)").toPandas().to_dict(orient="records") #pyspark -> pandas -> python dict conversion


    spark.stop()
    return result
