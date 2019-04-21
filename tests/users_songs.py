'''
Tests if code can fetch song Ids of user's top most listened to songs
Printes recommended list of songs based on above
Input user ID number for username
'''

import spotipy
import spotipy.util as util
import json
from json import JSONDecodeError

username = 'X'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

print()

results = spotifyObject.current_user_top_tracks(limit=5)

songName = results['items'][0]['name']
songID = results['items'][0]['id']

topSongs = []
print("You top songs:")
for i, item in enumerate(results['items']):
            topSongs.append(item['artists'][0]['id'])

print(topSongs)
print()

#for i, item in enumerate(results['items']):
#            print(item['name'], ' - ', item['artists'][0]['name'])


recs = spotifyObject.recommendations(seed_tracks=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
print("List of recommended songs based on your request:")
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])
recs = spotifyObject.recommendations(seed_artists=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])



#print(json.dumps(results,sort_keys=True,indent=4))

