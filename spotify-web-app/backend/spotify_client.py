# ==============================================================================
# SPOTIFY API CLIENT
# ==============================================================================
# Calls the Spotify API to get user profile, playlists, and tracks
# Requires users to login with their Spotify account
# The program uses the Spotipy Python library to interact with the API
# 
# Documentation:
# - Spotipy Python library: https://spotipy.readthedocs.io/en/2.25.1/#
# - Spotify Web API: https://developer.spotify.com/documentation/web-api/
# ==============================================================================

# ==============================================================================
# Modules
# ==============================================================================
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


# ==============================================================================
# Global Variables
# ==============================================================================

# Load environment variable from .env file
load_dotenv()

# Access API key
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')

# Scope: What data we want from the user's account
scope = "playlist-read-private playlist-modify-public playlist-modify-private user-library-read"

# sp: data from Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope=scope))


# ==============================================================================
# FUNCTION IMPLEMENTATION
# ==============================================================================

def get_user_profile(sp) -> dict:
    # Get the current user's profile information
    # Display name, external URLs, followers, etc.
    user_profile = sp.current_user()
    return user_profile


def get_user_playlist(sp) -> dict:
    # Get the current user's playlists
    user_playlists = sp.current_user_playlists(limit = 50)

    # Printing playlist names and IDs - debugging
    for playlist in user_playlists['items']:
        print(f"{playlist['name']} - {playlist['id']}")
    
    return user_playlists


def get_playlist_tracks(sp, playlist_id: str) -> dict:
    # Get tracks from a specific playlist
    results = sp.playlist_tracks(playlist_id)

    # Printing track names and artists - debugging
    for item in results['items']:
        track = item['track']
        print(f"{track['name']} by {track['artists'][0]['name']}")
    
    return results



def main() -> None:
    # Get user profile
    # In case we want UX to refer to the user's name, etc.
    user_profile = get_user_profile(sp)
    # print(user_profile)


    # Get tracks from a specific playlist
    playlist_id = get_user_playlist(sp)['items'][1]['id']
    playlist_tracks = get_playlist_tracks(sp, playlist_id)




if __name__ == "__main__":
    main()