import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_playlist(selected_songs, playlist_name, playlist_length):
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")


    scope = 'playlist-modify-public'
    username = '1230947442'
    token = SpotifyOAuth(scope=scope, username=username)
    spotifyObject = spotipy.Spotify(auth_manager = token)

    # create playlist
    
    playlist_description = "consensus playlist"


    spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

    
    list_of_songs = []

    for song in selected_songs:        
        result = spotifyObject.search(q=song.song_name)
        # print(json.dumps(result,sort_keys=4,indent=4))
        list_of_songs.append(result['tracks']['items'][0]['uri'])
        

    # find the new playlist
    prePlayList = spotifyObject.user_playlists(user=username)
    print(prePlayList)
    playlist = prePlayList['items'][0]['id']

    # add songs
    spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)


