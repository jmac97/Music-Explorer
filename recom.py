import spotipy
import spotipy.util as util

recs = []

#Prints header for list of songs
def callOut():
    print("\nList of recommended songs based on your request:")

#Prints song Name - Artist
def printRecs(list, total):
    for track in list['tracks']:
        total.append(track['id'])
        print("  >>>", track['name'], '-', track['artists'][0]['name'])

#Gets recommendations based on inputs
def getRecs(self, sp, type, list):
    recs = []

    if type == 'song':
        recs = sp.recommendations(seed_tracks=[self])
        callOut()
        printRecs(recs, list)
        recs = sp.recommendations(seed_tracks=[self])
        printRecs(recs, list)

    if type == 'artist':
        recs = sp.recommendations(seed_artists=[self])
        callOut()
        printRecs(recs, list)
        recs = sp.recommendations(seed_artists=[self])
        printRecs(recs, list)

    if type == 'genre':
        recs = sp.recommendations(seed_genres=[self])
        callOut()
        printRecs(recs, list)
        recs = sp.recommendations(seed_artists=[self])
        printRecs(recs, list)

#Creates and populates a playlist
def playlist(username, sp, list):
    name = input("Enter a name for the playlist: ")
    print("Please wait...")

    #Creates playlist based on that name and populates the playlist
    playlists = sp.user_playlist_create(username, name, public=True, description="Recommended Songs")
    for track in list:
        add = sp.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
    
    print("Check your Spotify account for your new playlist!")
