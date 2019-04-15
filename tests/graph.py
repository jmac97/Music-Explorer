import spotipy
import spotipy.util as util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

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

    s = pd.Series([artist['genres']])
    print()
    data = []
    for x in range(len(artist['genres'])):
        data.append(int(artist['genres'][x].count(str(artist['genres'][x]))))
    print(data)
    print(artist['genres'])
    print(len(artist['genres']))

    df = pd.DataFrame({'Genres': artist['genres'], 'amount': data})
    ax = df.plot.bar(x='Genres', y='amount',rot=0)

    #df = pd.DataFrame({'lab':list(artist['genres']), 'val': data})
    #ax = df.plot(kind='bar', title ="Genre Spread", figsize=(15, 10), legend=True, fontsize=12)
    plot.show()
        