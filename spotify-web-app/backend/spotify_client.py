# ==============================================================================
# SPOTIFY API CLIENT
# ==============================================================================
# Calls the Spotify API to get user profile, playlists, and tracks
# Requires users to login with their Spotify account
# The program uses the Spotipy Python library to interact with the API
# ==============================================================================

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access API keys
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

# Scope: What data we want from the user's account
SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-read user-top-read user-read-recently-played"


# ==============================================================================
# AUTHENTICATION FUNCTIONS
# ==============================================================================

def create_spotify_oauth(redirect_uri: str):
    # Create Spotify oauth object
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )

def refresh_token_if_expired(sp_oauth, token_info):
    # Refresh token if expired
    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


# ==============================================================================
# SPOTIFY API FUNCTIONS
# ==============================================================================

def get_user_profile(sp) -> dict:
    # Get user profile
    user_profile = sp.current_user()
    # print(user_profile)
    return user_profile


def get_user_playlists(sp, limit=50) -> list:
    # Get user's playlists
    user_playlists = sp.current_user_playlists(limit=limit)
    # print('---')
    # print(user_playlists['items'])
    return user_playlists['items']


def get_playlist_tracks(sp, playlist_id: str) -> list:
    # Get tracks in a specific playlist
    results = sp.playlist_tracks(playlist_id)
    
    tracks = []
    for item in results['items']:
        track = item['track']
        if track and track['id']:
            tracks.append({
                'id': track['id'],
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'uri': track['uri']
            })
    
    return tracks


def get_top_tracks(sp, limit=10, time_range='short_term') -> list:
    # Get user's top tracks
    results = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    
    tracks = []
    for item in results['items']:
        tracks.append({
            'name': item['name'],
            'artist': item['artists'][0]['name']
        })
    
    return tracks


def get_recently_played(sp, limit=10) -> list:
    # Get user's recently played tracks
    results = sp.current_user_recently_played(limit=limit)
    
    tracks = []
    for item in results['items']:
        tracks.append({
            'name': item['track']['name'],
            'artist': item['track']['artists'][0]['name'],
            'album': item['track']['album']['name']
        })
    
    return tracks