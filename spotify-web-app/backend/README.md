# Backend README for Spotify Web App

# Spotify Web App - Backend

This is the backend component of the Spotify Web App, built using Flask and the Spotipy library to interact with the Spotify API.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd spotify-web-app/backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the `backend` directory with the following content:
   ```
   client_id=<your_spotify_client_id>
   client_secret=<your_spotify_client_secret>
   redirect_uri=<your_redirect_uri>
   ```

## Running the Application

To start the Flask server, run the following command:
```
python app.py
```

The backend will be available at `http://localhost:5000`.

## Usage

The backend provides endpoints to interact with the Spotify API. You can use the `/saved-tracks` endpoint to retrieve the user's saved tracks.

## License

This project is licensed under the MIT License.