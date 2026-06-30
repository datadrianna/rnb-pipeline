import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd

# Load credentials from .env file
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Connect to Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Our list of 90s/2000s R&B artists
artists = ["Aaliyah", "TLC", "Destiny's Child", "Usher", "Missy Elliott", "Brandy", "Mary J. Blige"]

all_tracks = []

for artist_name in artists:
    print(f"Searching for {artist_name}...")
    
    # Find the artist
    results = sp.search(q=artist_name, type="artist", limit=1)
    if not results["artists"]["items"]:
        print(f"  Could not find {artist_name}")
        continue
    artist = results["artists"]["items"][0]
    artist_id = artist["id"]
    
    # Get their albums
    albums = sp.artist_albums(artist_id, album_type="album", limit=10)
    
    for album in albums["items"]:
        album_name = album["name"]
        release_date = album["release_date"]
        
        # Get tracks for this album
        tracks = sp.album_tracks(album["id"])
        
        for track in tracks["items"]:
            all_tracks.append({
                "artist": artist_name,
                "album": album_name,
                "release_date": release_date,
                "track_name": track["name"],
                "track_number": track["track_number"],
                "duration_ms": track["duration_ms"]
            })

# Convert to a dataframe and save
df = pd.DataFrame(all_tracks)
df.to_csv("raw_tracks.csv", index=False)

print(f"\nDone! Pulled {len(df)} tracks total.")
print(df['artist'].value_counts())
print(df.head())