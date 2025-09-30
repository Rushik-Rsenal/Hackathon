from flask import Flask, jsonify, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

@app.route('/api/saved_tracks', methods=['GET'])
def get_saved_tracks():
    results = sp.current_user_saved_tracks()
    tracks = [{'artist': item['track']['artists'][0]['name'], 'name': item['track']['name']} for item in results['items']]
    return jsonify(tracks)

if __name__ == '__main__':
    app.run(debug=True)