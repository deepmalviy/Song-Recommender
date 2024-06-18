import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')


# Define the scope to access user playlists
scope = 'playlist-read-private playlist-read-collaborative'

# Authentication - user login
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Get current user's playlists
playlists = sp.current_user_playlists()

# Initialize a list to store track data
data = []

for playlist in playlists['items']:
    playlist_name = playlist['name']
    playlist_id = playlist['id']
    
    # Get tracks from the playlist
    tracks = sp.playlist_tracks(playlist_id)
    
    for track in tracks['items']:
        # Extract track information
        track_uri = track['track']['uri']
        track_name = track['track']['name']
        artist_uri = track['track']['artists'][0]['uri']
        artist_info = sp.artist(artist_uri)
        artist_name = track['track']['artists'][0]['name']
        artist_pop = artist_info['popularity']
        artist_genres = artist_info['genres']
        album = track['track']['album']['name']
        track_pop = track['track']['popularity']
        audio_features = sp.audio_features(track_uri)[0]
        
        # Append data to the list
        data.append({
            'playlist_name': playlist_name,
            'track_uri': track_uri,
            'track_name': track_name,
            'artist_name': artist_name,
            'artist_popularity': artist_pop,
            'artist_genres': artist_genres,
            'album': album,
            'track_popularity': track_pop,
            **audio_features  # Add all audio features as individual columns
        })

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file (optional)
df.to_csv('spotify_tracks_f.csv', index=False)
