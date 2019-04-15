import spotipy
import spotipy.util as util

# User ID: 1224649854

print("Welcome to Pioneer Playlist!")
print()
print(">>> Type 'start' to begin")
print()
print(">>> Type anything else to exit the program")
print()
start = input("Your input: ")

if start == 'start':
    print()
    number = input("Enter your user ID: ")

    username = number

    token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')
    
    spotifyObject = spotipy.Spotify(auth=token)
    spotifyObject.trace = False

    user = spotifyObject.current_user()

    displayName = user['display_name']

    while True:
        print()
        print(">>> Welcome " + displayName + "!")
        print()
        name = input("Enter name of an artist or type 'close program' to leave: ")
        print()

        if name == 'close program':
            print()
            print("Goodbye!")
            break

        searchResults = spotifyObject.search(name,1,0,"artist")
        artist = searchResults['artists']['items'][0]

        print("Your serarch request: " + artist['name'])
        print("They have " + str(artist['followers']['total']) + " followers")
        print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2])
        print()
        artistID = artist['id']

        recs = spotifyObject.recommendations(seed_artists=[artist['id']])
        print("List of recommended songs based on your request:")
        for track in recs['tracks']:
            print(track['name'], '-', track['artists'][0]['name'])
        recs = spotifyObject.recommendations(seed_artists=[artist['id']])
        for track in recs['tracks']:
            print(track['name'], '-', track['artists'][0]['name'])
        
        print()
        print("Would you like to make this a playlist?")
        print("Type 'Yes' or 'No'")
        print()
        answer = input("Your choice: ")

        if answer == 'Yes':
            name = input("Enter a name for the playlist: ")
            print()
            playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
            for track in recs['tracks']:
                add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track['id']], position=None)

    
else:
    print()
    print("Goodbye!")