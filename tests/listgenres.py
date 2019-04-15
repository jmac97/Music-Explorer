import spotipy
import spotipy.util as util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

import json
from json.decoder import JSONDecodeError

plot.close('all')

# User ID: 1224649854
username = '1224649854'

token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')
    
spotifyObject = spotipy.Spotify(auth=token)
spotifyObject.trace = False

user = spotifyObject.current_user()

while True:
    name = input("Enter name of an artist or type 'close program' to leave: ")
    print()

    searchResults = spotifyObject.search(name,1,0,"artist")
    artist = searchResults['artists']['items'][0]

    print("Your serarch request: " + artist['name'])
    print("They have " + str(artist['followers']['total']) + " followers")
    print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2])
    print()
    artistID = artist['id']

    recs = spotifyObject.recommendations(seed_artists=[artist['id']])
    print("List of recommended songs based on your request:")
    ids = []
    for track in recs['tracks']:
        print(track['name'], '-', track['artists'][0]['name'])
    recs = spotifyObject.recommendations(seed_artists=[artist['id']])
    for track in recs['tracks']:
        print(track['name'], '-', track['artists'][0]['name']) 

    for x in track['id']:
        print(x)   