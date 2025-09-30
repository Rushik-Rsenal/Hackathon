import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SpotifyPlayer = () => {
    const [tracks, setTracks] = useState([]);

    useEffect(() => {
        const fetchTracks = async () => {
            try {
                const response = await axios.get('/api/saved-tracks');
                setTracks(response.data);
            } catch (error) {
                console.error('Error fetching tracks:', error);
            }
        };

        fetchTracks();
    }, []);

    return (
        <div>
            <h2>Saved Tracks</h2>
            <ul>
                {tracks.map((track, index) => (
                    <li key={index}>
                        {track.artist} - {track.name}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SpotifyPlayer;