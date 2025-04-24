import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def fetch_top_tracks(artist_name):
    output_path=f"data/{artist_name}.json"
    sp = get_spotify_client()
    result = sp.search(q=artist_name, type='artist')
    
    if not result['artists']['items']:
        print("Artist not found.")
        return
    print("result:", result)
    artist_id = result['artists']['items'][0]['id']
    tracks = sp.artist_top_tracks(artist_id)

    with open(output_path, "w") as f:
        json.dump(tracks['tracks'], f, indent=4)
    
    print(f"Top tracks for {artist_name} saved to {output_path}")
