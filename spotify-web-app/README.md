# Spotify Web App

This project is a web application that integrates with the Spotify API, allowing users to interact with their Spotify library through a Flask backend and a React frontend.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using Flask and is responsible for handling API requests to Spotify.

- **app.py**: The main entry point for the Flask application. It sets up the application, configures routes, and handles requests to the Spotify API.
- **requirements.txt**: Lists the Python dependencies required for the backend, including Flask and Spotipy.
- **.env**: Contains environment variables such as the Spotify API credentials (client_id, client_secret, redirect_uri) needed for authentication.
- **README.md**: Documentation for the backend, including setup instructions and usage details.

### Frontend

The frontend is built using React and provides the user interface for the application.

- **public/index.html**: The main HTML file for the React application. It serves as the entry point for the React app and includes the root div where the React components will be rendered.
- **src/App.jsx**: The main React component that serves as the root of the application. It manages the overall layout and routing of the app.
- **src/index.jsx**: The entry point for the React application. It renders the `App` component into the DOM.
- **src/components/SpotifyPlayer.jsx**: A React component that interacts with the Spotify API to display and control music playback.
- **package.json**: The configuration file for npm. It lists the dependencies, scripts, and metadata for the React frontend.
- **README.md**: Documentation for the frontend, including setup instructions and usage details.

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Spotify API credentials.
4. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the web application in your browser. The frontend will communicate with the backend to fetch and display data from the Spotify API.