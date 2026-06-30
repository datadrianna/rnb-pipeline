import pandas as pd
import sqlite3
import boto3
from dotenv import load_dotenv
import os

# Load credentials from .env file
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Load our cleaned data
df = pd.read_csv("clean_tracks.csv")

# Connect to a SQLite database (creates the file if it doesn't exist yet)
conn = sqlite3.connect("rnb_music.db")

# Write the dataframe into a table called "tracks"
df.to_sql("tracks", conn, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into rnb_music.db")

# Quick test query to confirm it worked
result = pd.read_sql("SELECT artist, COUNT(*) as track_count FROM tracks GROUP BY artist", conn)
print(result)

conn.close()

# Upload CSVs to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

bucket_name = "datadrianna-rnb-pipeline"

s3.upload_file("raw_tracks.csv", bucket_name, "raw_tracks.csv")
s3.upload_file("clean_tracks.csv", bucket_name, "clean_tracks.csv")

print(f"Uploaded CSVs to S3 bucket: {bucket_name}")