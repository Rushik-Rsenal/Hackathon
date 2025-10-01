from flask import Flask, render_template, redirect, request, session, url_for
from spotify_client import create_spotify_oauth, refresh_token_if_expired, get_user_profile, get_user_playlists
import spotipy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', os.urandom(24))


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_token():
    # Token
    token_info = session.get('token_info', None)
    if not token_info:
        return None
    
    # Refresh token if expired
    sp_oauth = create_spotify_oauth(url_for('callback', _external=True))
    token_info = refresh_token_if_expired(sp_oauth, token_info)
    session['token_info'] = token_info
    
    return token_info


def get_spotify_client():
    # Get Spotify client
    token_info = get_token()
    if not token_info:
        return None
    return spotipy.Spotify(auth=token_info['access_token'])


# ==============================================================================
# ROUTES
# ==============================================================================

@app.route('/')
def index():
    # Home page
    if get_token():
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/login')
def login():
    # Redirect the user to the Spotify login page to authorize our app
    sp_oauth = create_spotify_oauth(url_for('callback', _external=True))
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # Callback user from the Spotify login page into our page
    sp_oauth = create_spotify_oauth(url_for('callback', _external=True))
    session.clear()
    
    # Get authorization code
    code = request.args.get('code')
    
    # Exchange code for tokens
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    # User dashboard
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('login'))
    
    try:
        # Get user info and playlists
        user = get_user_profile(sp)
        playlists = get_user_playlists(sp, limit=50)
        
        # Pass data to template
        return render_template('dashboard.html', 
                             user=user, 
                             playlists=playlists)
    except Exception as e:
        return f"Error loading dashboard: {str(e)}", 500


@app.route('/logout')
def logout():
    # Logout
    session.clear()
    return redirect(url_for('index'))


# ==============================================================================
# RUN APPLICATION
# ==============================================================================

if __name__ == '__main__':
    # Check if environment variables are set
    if not os.getenv('SPOTIFY_CLIENT_ID') or not os.getenv('SPOTIFY_CLIENT_SECRET'):
        print("❌ Error: Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in .env file")
        exit(1)
    
    print("✅ Starting Flask application...")
    app.run(debug=True, port=5000)