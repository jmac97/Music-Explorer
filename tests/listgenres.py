import spotipy
import spotipy.util as util
import json
from json import JSONDecodeError


# User ID: 1224649854
username = '1224649854'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')
    
spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

user = spotifyObject.current_user()


gdict =  spotifyObject.recommendation_genre_seeds()
    
#print(json.dumps(genres,sort_keys=True,indent=4))

genres = list(gdict.values())
ugh = genres[0]

for i in ugh:
    print(i)