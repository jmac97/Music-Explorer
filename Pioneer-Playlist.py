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

    token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id='39072f510ea74d4781f2423c61bb4c27',client_secret='82a83ddeb06743e0956bcbb296856412',redirect_uri='https://www.google.com/')
    
    spotifyObject = spotipy.Spotify(auth=token)
    spotifyObject.trace = False

    user = spotifyObject.current_user()

    displayName = user['display_name']

    while True:
        print()
        print("Welcome " + displayName + "!")
        print()
        print("Enter number of menu choice.")
        print()
        print(">>> 1: Search for a song")
        print()
        print(">>> 2. Search for an artist")
        print()
        print(">>> 3. Search for a genre")
        print()
        print(">>> 4. Your top songs")
        print()
        print(">>> 5. Your top artists")
        print()
        choice = input("Your choice: ")
        print()

        if choice == 'close program':
            print()
            print("Goodbye!")
            break
        
        
        if choice == '1':
            searchResults = spotifyObject.search(choice,1,0,"track")

            artist = searchResults['tracks']['items'][0]['artists'][0]['name']
            song = searchResults['tracks']['items'][0]['name']

            print("Your serarch request: " + song, ' - ', artist)
            print()

            recs = spotifyObject.recommendations(seed_tracks=[songID])
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                print(track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_tracks=[songID])
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
        
        if choice == '2':
            searchResults = spotifyObject.search(choice,1,0,"artist")
            artist = searchResults['artists']['items'][0]

            print("Your serarch request: " + artist['name'])
            print("They have " + str(artist['followers']['total']) + " followers")
            print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2])
            print("List of their top songs:")
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
        
        if choice == '3':
            print("Here are the possible list of genres to search for: ")
            print()
            gdict =  spotifyObject.recommendation_genre_seeds()

            genres = list(gdict.values())
            ugh = genres[0]

            for i in ugh:
                print(i)
            
            print()
            print("Enter up to five of the above genres, seperating by commas")
            genreChoice = input("Your choice: ")

            recs = spotifyObject.recommendations(seed_genres=[genreChoice])
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                print(track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_genres=[genreChoice])
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
        
        if choice == '4':
            results = spotifyObject.current_user_top_tracks(5)

            songName = results['items'][0]['name']
            songID = results['items'][0]['id']

            topSongs = []

            print("Your top five songs:")
            for i, item in enumerate(results['items']):
                topSongs.append(item['artists'][0]['id'])
                print(item['name'], ' - ', item['artists'][0]['name'])
            
            print()
            recs = spotifyObject.recommendations(seed_tracks=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
            print("List of recommended songs based on your top songs:")
            for track in recs['tracks']:
                print(track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_artists=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
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
        
        if choice == '5':
            results = spotifyObject.current_user_top_artists(limit=5)

            topArtists = []

            print("List of your top artists:")
            for item in results['items']:
                topArtists.append(item['id'])
                print(item['name'])
            
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                print(track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
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