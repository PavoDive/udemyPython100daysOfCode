import requests
from bs4 import BeautifulSoup
from password import client_id, client_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#---------------- Get user date ----------------
desired_date = input("Input the date you want to travel to (YYYY-MM-DD): ")

#---------------- Get the songs ----------------
# this is the format of the url
# https://www.billboard.com/charts/hot-100/2000-08-12/

billboard_url = f"https://www.billboard.com/charts/hot-100/{desired_date}/"

# I may need the year to search for the song
song_year = desired_date.split("-")[0]

print(f"We are collecting the hottest 100 songs of {desired_date}. Please wait...")
response = requests.get(url = billboard_url)
response.raise_for_status()

sp = BeautifulSoup(response.text, "html.parser")

# titles are <h3> with class "a-no-trucate" and id "title-of-a-story"
h3 = sp.find_all(name = "h3", id = "title-of-a-story", class_ = "a-no-trucate")

# This is the list of 100 songs
songs = [" ".join(song.string.split()) for song in h3]

#---------------- Authenticate to Spotify ----------------

print("Authenticating with Spotify...")

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret = client_secret, scope=scope, redirect_uri="http://example.com"))

user_name = sp.me()["uri"].split(":")[2]

# create playlist
print("Creating the playlist...")
playlist_name = f"Top 100 of {desired_date}"
a = sp.user_playlist_create(user = user_name, name = playlist_name)
playlist_id = a["uri"].split(":")[2]
# ---------------- Search for and Add Songs ----------------


for song in songs:
    result = sp.search(q = f"track:{song} year:{song_year}")
    try:
        song_id = result["tracks"]["items"][0]["id"]
    except IndexError:
        next
    else:
        print(f"Adding <<{song}>> to the playlist.")
        sp.user_playlist_add_tracks(user_name, playlist_id = playlist_id, tracks = [song_id])



