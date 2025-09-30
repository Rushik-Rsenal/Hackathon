import spotipy
from dotenv import load_dotenv
import os

# Load environment variable from .env file
load_dotenv()

# Access API key
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')

# Scope: What data we want from the user's account
scope = "user-library-read"

# sp: data from Spotify API client
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                                       client_secret=client_secret,
                                                       redirect_uri=redirect_uri,
                                                       scope=scope))


results = sp.current_user_saved_tracks()

# Output the names of recently saved tracks
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}. {track['artists'][0]['name']} - {track['name']}")
