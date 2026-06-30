import pandas as pd
import sqlite3

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