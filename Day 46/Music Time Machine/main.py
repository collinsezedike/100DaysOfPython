import requests
from bs4 import BeautifulSoup
import spotipy


URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "eb82732fc44842dea1ce6a9fd710ba2a"
CLIENT_SECRET = "d69383c961dc40669a6817e352584896"
USER_ID = "31wsgt33uej5ldl3xvwoy4veqiau"

# timeline = input("What year do you want to travel to? Type the date in this format: YYYY-MM-DD ")
timeline = "2022-02-24"

# fetch songs
response = requests.get(f"{URL}{timeline}")
response.raise_for_status()
songs_html = response.text

soup = BeautifulSoup(songs_html, "html.parser")
all_songs = soup.findAll(name="h3", class_="a-no-trucate")
songs = [song_tag.getText().strip() for song_tag in all_songs]

# spotipy authentication
sp_auth = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
)

# a spotipy object initialization
sp = spotipy.Spotify(auth_manager=sp_auth)
print("Spotify object initialized")

# get songs URIS
songs_URIS = []
for song in songs:
    search_result = sp.search(q=f"track:{song} year:{timeline.split('-')[0]}", type="track")
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
    except IndexError:
        pass
    else:
        songs_URIS.append(uri)
print("URIs list created")
# create a new playlist
playlist = sp.user_playlist_create(USER_ID, name=f"{timeline} Billboard 100",
                                   public=False, description=f"Hot 100 songs for {timeline}")
print("Playlist created")

# add tracks to playlist
sp.playlist_add_items(playlist["id"], items=songs_URIS)
print("Added songs")

