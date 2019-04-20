import spotipy
import spotipy.util as util
import json
from json import JSONDecodeError

# User ID: 1224649854

username = '1224649854'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

choice = input("Your choice: ")
print()

searchResults = spotifyObject.search(choice,1,0,"track")

artist = searchResults['tracks']['items'][0]['artists'][0]['name']
song = searchResults['tracks']['items'][0]['name']
songID = searchResults['tracks']['items'][0]['id']


print("Your serarch request: " + song, ' - ', artist)
print()

#print(json.dumps(searchResults,sort_keys=True,indent=4))


recs = spotifyObject.recommendations(seed_tracks=[songID])
print("List of recommended songs based on your request:")
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])
recs = spotifyObject.recommendations(seed_tracks=[songID])
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])
