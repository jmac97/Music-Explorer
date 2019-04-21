'''
Tests fetching user id and necessary API credentials
Tests if username will be displayed
'''

import spotipy
import sys
import spotipy.util as util

username = sys.argv[1]

try: 
    token = util.prompt_for_user_token(username,client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')

except:
    os.remove(f".cache-(username)")
    token = util.prompt_for_user_token(username,client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']

print(displayName)
