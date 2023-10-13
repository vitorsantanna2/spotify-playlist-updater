import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import base64
with open("./data/photo.png", "rb") as img_file:
    myimage = base64.b64encode(img_file.read())
load_dotenv()
print("Starting Playlist updater")
def func():
    scope = 'playlist-modify-public ugc-image-upload'

    username = os.environ['USER_SPOTIFY']
    print("USERNAME OK")
    SPOTIPY_CLIENT_ID = os.environ['CLIENT_ID']
    print("client id OK")
    SPOTIPY_CLIENT_SECRET = os.environ['CLIENT_SECRET']
    print("client secret OK")
    redirect_uri = os.environ['REDIRECT_URI']
    print("redirect uri OK")
    token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri)
    print("TOKEN OK")
    sp = spotipy.Spotify(auth=token)

    # Playlist Data
    id = os.environ['PLAYLIST_ID']
    playlist_name = 'new_playlist'
    playlist_description = 'playlist_one'
    image_b64 = myimage

    sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
    sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)

    print("Playlist updated")

func()
#You can replace minutes with seconds, hours, etc
