import pandas as pd

# Load the raw data we extracted
df = pd.read_csv("raw_tracks.csv")

print(f"Starting with {len(df)} rows")

# Remove duplicate tracks (same artist + same track name)
df = df.drop_duplicates(subset=["artist", "track_name"])
print(f"After removing duplicates: {len(df)} rows")

# Convert release_date from text into an actual date format
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Convert duration from milliseconds into minutes (easier to read)
df["duration_minutes"] = (df["duration_ms"] / 60000).round(2)

# Extract just the year for easier analysis later
df["release_year"] = df["release_date"].dt.year

# Save the cleaned version
df.to_csv("clean_tracks.csv", index=False)

print("Saved clean_tracks.csv")
print(df.head())