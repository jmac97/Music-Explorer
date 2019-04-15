import spotipy
import spotipy.util as util
import json
from json.decoder import JSONDecodeError
import genres

# User ID: 1224649854


username = '1224649854'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-read-recently-played ', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')
    
spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

user = spotifyObject.current_user()

recents = spotifyObject.current_user_recently_played(50)
song = recents['items'][0]['track']
print(json.dumps(song,sort_keys=True,indent=4))

#for x in recents[]:
 #   song = [recents['items'][0]['track']['name']]
  #  print(song)
   # item += 1


#recs = spotifyObject.recommendations(seed_tracks=[song['id']])
#print("List of recommended songs based on your request:")
#for track in recs['tracks']:
 #   print(track['name'], '-', track['artists'][0]['name'])


#print(str(recents['items'][0]['track']['name']) + " - " + str(recents['items'][0]['track']['artists'][0]['name']))

#print(json.dumps(recents,sort_keys=True,indent=4))