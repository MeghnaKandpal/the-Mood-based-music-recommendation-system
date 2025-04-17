import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-public playlist-modify-private"
))

emotion_to_mood = {
    "happy": ["upbeat", "energetic"],
    "sad": ["calm", "relaxed"],
    "neutral": ["chill"]
}


def get_songs(mood):
    results = sp.search(q=mood, type="track", limit=10)
    songs = []
    for track in results['tracks']['items']:
        songs.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify'],
            'uri': track['uri']  
        })
    return songs

def recommend_songs(emotion):
    mood_list = emotion_to_mood.get(emotion, ["chill"])
    all_songs = []
    for mood in mood_list:
        songs = get_songs(mood)
        all_songs.extend(songs)
    return all_songs

def create_playlist_with_songs(emotion, songs):
    username = '31jgf3sbidcuomui45dbhzg4hhue'
    new_playlist = sp.user_playlist_create(user=username, name=f"{emotion.capitalize()} Songs", public=True)
    song_uris = [song['uri'] for song in songs]
    playlist_id = new_playlist['id']
    sp.playlist_add_items(playlist_id, song_uris)
    
    return f"https://open.spotify.com/playlist/{playlist_id}"
