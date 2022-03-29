import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env")

sp=spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"]))

def fetch_playlist(USER_ID, PLAYLIST_ID):
    """ Fecth specific playlist from a user on Spotify.
    """
    # Create empty dataframe
    playlist_features_list = ["artist","album","track_name",  "track_id","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]

    playlist_df = pd.DataFrame(columns = playlist_features_list)

    # Loop through every track in the playlist, extract features and append the features to the playlist df

    playlist = sp.user_playlist_tracks(USER_ID, PLAYLIST_ID)["tracks"]["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
    # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
    
    return playlist_df

# Save data
df = fetch_playlist(config["USER_ID"], config["PLAYLIST_ID"])
df.to_csv("data/spotify_playlist.csv", index = False)
df.to_sql("data/spotify_playlist.csv", index = False)
