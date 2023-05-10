import json
import requests
import time
import zipfile
import os
from tqdm import tqdm
import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'ed81fe4aba8e41f28536c55f1ecdb7b0'
client_secret = 'cf68d5e7365b406f916c166400e743e6'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# The URL of the playlist
playlist_url = 'https://open.spotify.com/playlist/6FKDzNYZ8IW1pvYVF4zUN2?si=d61087039b6f4784'

# Extract the playlist id from the URL
playlist_id = playlist_url.split('/')[-1].split('?')[0]

# Create the directory for the album covers if it doesn't already exist
os.makedirs('albumcoverimages', exist_ok=True)

# Initialize an empty list to store the data
data = []

# The number of tracks per page
limit = 100

# The initial offset
offset = 0

while True:
    # Get the tracks in the playlist
    results = sp.playlist_items(playlist_id, offset=offset, limit=limit)

    # Break out of the loop if no more tracks are returned
    if not results['items']:
        break

    # Loop over each track in the playlist
    for item in results['items']:
        track = item['track']
        
        # Sanitize the track name to use it as a filename
        safe_track_name = re.sub(r'[\/:*?"<>|]', '', track['name'])
        album_cover_path = f"albumcoverimages/{safe_track_name}_cover.jpg"

        # Check if the album cover already exists
        if not os.path.exists(album_cover_path):
            # Get the audio features for the track
            audio_features = sp.audio_features(track['id'])[0]

            # Check if the track has an album cover
            if track['album']['images']:
                # Add the album cover URL to the data
                audio_features['album_cover_url'] = track['album']['images'][0]['url']

                # Save the album cover
                album_cover_response = requests.get(track['album']['images'][0]['url'])
                with open(album_cover_path, 'wb') as f:
                    f.write(album_cover_response.content)
            else:
                audio_features['album_cover_url'] = None

            # Append the data to the list
            data.append(audio_features)

    # Increase the offset by the limit
    offset += limit

# Write the data to a JSON file
with open('playlist_data.json', 'w') as f:
    json.dump(data, f)