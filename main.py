import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import cid, secret

# Authentication
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def grabber(playlist_link):
    # Grab URI from playlist link
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    track_uris = [x['track']['uri'] for x in sp.playlist_tracks(playlist_URI)['items']]
    
    dict = {
        'track_uri':[],
        'track_name':[],
        'artist_uri':[],
        'artist_info':[],
        'artist_name':[],
        'artist_pop':[],
        'artist_genres':[],
        'album':[],
        'track_pop':[],
    }
    
    # Search through playlist tracks for relevant info
    for track in sp.playlist_tracks(playlist_URI)['items']:
        tr = track['track']
        #URI
        track_uri = tr['uri']
        dict['track_uri'].append(track_uri)
        
        #Track name
        track_name = tr['name']
        dict['track_name'].append(track_name)
        
        #Main Artist
        artist_uri = tr['artists'][0]['uri']
        artist_info = sp.artist(artist_uri)
        dict['artist_uri'].append(artist_uri)
        dict['artist_info'].append(artist_info)
        
        #Name, Popularity, Genre
        artist_name = tr['artists'][0]['uri']
        artist_pop = artist_info['popularity']
        artist_genres = artist_info['genres']
        
        dict['artist_name'].append(artist_name)
        dict['artist_pop'].append(artist_pop)
        dict['artist_genres'].append(artist_genres)
        
        #Album
        album = tr['album']['name']
        dict['album'].append(album)
        
        #Popularity of track
        track_pop = tr['popularity']
        dict['track_pop'].append(track_pop)
        
        #audio features
        # audio_features = sp.audio_features(track_uri)
    return dict


# dict = {
#     'uri':track_uri,
#     'name':track_name,
#     'artist_uri':artist_uri,
#     'artist_info':artist_info,
#     'artist_name':artist_name,
#     'artist_pop':artist_pop,
#     'artist_genres':artist_genres,
#     'album':album,
#     'track_pop':track_pop,
# }