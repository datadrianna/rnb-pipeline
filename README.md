# 90s/2000s R&B ETL Pipeline

A data pipeline that extracts, cleans, and stores track data for iconic 90s and 2000s R&B artists using the Spotify API.

## WHY?

I'm a data analyst working towards becoming a data enginner, and I wanted to brush up on my skills! This project pulls discography data for artists like Aaliyah, TLC, Destiny's Child, Usher, Missy Elliott, Brandy, and Mary J. Blige, and turns it into a clean dataset.

## WHAT DOES IT DO?

1. ('extract.py') Connects to the Spotify API and pulls every album and track for a list of artists.
2. ('transform.py') Cleans the raw data: removes duplicate tracks (deluxe editions, remasters), converts release dates into usable date formats, and calculates track duration in minutes.
3. ('load.py') Loads the cleaned data into a SQLite database ('rnb_music.db') for easy querying.

## STACK
- Python core language
- Spotipy Python wrapper for the Spotify Web API
- Pandas data cleaning and transformation
- SQLite lightweight database for storage

## RESULTS

Starting from raw Spotify data, the pipeline currently processes:
- 837 raw tracks pulled from Spotify
- 741 unique tracks after deduplication
- 7 artists fully cataloged

## HOW-TO

1. Clone this repo
2. Create a virtual environment and install 
    bash
        python3 -m venv venv
        source venv/bin/activate
        pip3 install -r requirements.txt
3. Create a '.env' file with your own Spotify API credentials:
    SPOTIFY_CLIENT_ID=your_client_id_here
    SPOTIFY_CLIENT_SECRET=your_client_secret_here
4. Run in order:
    bash
        python3 extract.py
        python3 transform.py
        python3 load.py

## built by [datadrianna]
