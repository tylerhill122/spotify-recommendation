import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import cid, secret

# Authentication
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Spotify global playlist
playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f'

# Grab URI from playlist link
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x['track']['uri'] for x in sp.playlist_tracks(playlist_URI)['items']]

# Search through playlist tracks for relevant info
for track in sp.playlist_tracks(playlist_URI)['items']:
    tr = track['track']
    #URI
    track_uri = tr['uri']
    
    #Track name
    track_name = tr['name']
    
    #Main Artist
    artist_uri = tr['artists'][0]['uri']
    artist_info = sp.artist(artist_uri)
    
    #Name, Popularity, Genre
    artist_name = tr['artists'][0]['uri']
    artist_pop = artist_info['popularity']
    artist_genres = artist_info['genres']
    
    #Album
    album = tr['album']['name']
    
    #Popularity of track
    track_pop = tr['popularity']
    
    #audio features
    # audio_features = sp.audio_features(track_uri)