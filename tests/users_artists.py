import spotipy
import spotipy.util as util
import json
from json import JSONDecodeError

# User ID: 1224649854

username = '1224649854'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

print()

results = spotifyObject.current_user_top_artists(limit=5)

topArtists = []


print("List of your top artists:")
for item in results['items']:
    topArtists.append(item['id'])
    print(item['name'])

#print(artistID)




#print(json.dumps(results,sort_keys=True,indent=4))


recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
print("List of recommended songs based on your request:")
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])
recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
for track in recs['tracks']:
    print(track['name'], '-', track['artists'][0]['name'])
