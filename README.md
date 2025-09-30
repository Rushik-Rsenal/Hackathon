https://developer.spotify.com/documentation/web-api

SORTIFY

Using the API requires a Spotify account.
Initial version will require that the user login with a spotify account.
Future versions might have a default Spotify account so users don't need to login for public Spotify playlists.

The user supplies a URL to their playlist, this can be easilly copied through the official Spotify app GUI.

The user is then provided with different sorting options based on the available metadata. The sorted playlist is saved as a new playlist on that user's account.


NO_LOGGIN_VERSION:
The app runs OUR own free Spotify account.
The front-page has a message "Only works with public playlists".
User supplies a URL to a public playlist.
OUR account generates a sorted version of the playlist and generates a URL to OUR new playlist.
The user can then use this URL to copy the sorted playlist to their own account.

This avoids the user needing to login to our shady website.
The user still needs to copy the shady link to our playlist?
It might be possible to identify the user if we can see which accounts copied from us.
