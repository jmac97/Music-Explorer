import spotipy
import spotipy.util as util
import config


print("Welcome to Pioneer Playlist!\n")
print(">>> Type 'Start' to begin")
print(">>> Type anything else to exit the program\n")
start = input("Your input: ")

if start == 'Start' or start == 'start':
    number = input("Enter your user ID: ")

    username = number

    token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=cID,client_secret=cSecret,redirect_uri='https://www.google.com/')
    
    spotifyObject = spotipy.Spotify(auth=token)
    spotifyObject.trace = False

    user = spotifyObject.current_user()

    displayName = user['display_name']

    while True:
        print("\n\nWelcome " + displayName + "!")
        print("We'll now create a playlist based on one of the below.")
        print("Enter the number of one of the menu choices:")
        print("  >>> 1: Search for a song")
        print("  >>> 2. Search for an artist")
        print("  >>> 3. Search for a genre")
        print("  >>> 4. Your top songs")
        print("  >>> 5. Your top artists\n")
        choice = input("Your choice: ")

        if choice == 'close program' or choice == 'Close Program' or choice == 'close Program' or choice == 'Close program':
            print()
            print("Goodbye!")
            break
        
        if choice == '1':
            choice = input("Enter a name of a song: ")
            searchResults = spotifyObject.search(choice,1,0,"track")

            artist = searchResults['tracks']['items'][0]['artists'][0]['name']
            song = searchResults['tracks']['items'][0]['name']
            songID = searchResults['tracks']['items'][0]['id']

            print("\n\nYour serarch request: " + song, ' - ', artist,"\n")

            recs = spotifyObject.recommendations(seed_tracks=[songID])
            allRecs = []
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_tracks=[songID])
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
        
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                name = input("Enter a name for the playlist: ")
                print("Please wait...")

                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in allRecs:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
                
                print("Check your Spotify account for your new playlist!")
        
        if choice == '2':
            choice = input("Enter name of an artist: ")
            searchResults = spotifyObject.search(choice,1,0,"artist")
            artist = searchResults['artists']['items'][0]

            print("\n\nYour serarch request: " + artist['name'])
            print("They have " + str(artist['followers']['total']) + " followers")
            print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2] + '\n')
            
            recs = spotifyObject.recommendations(seed_artists=[artist['id']])
            allRecs = []
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_artists=[artist['id']])
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
        
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                name = input("Enter a name for the playlist: ")
                print("Please wait...")
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in allRecs:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
            
            print("Check your Spotify account for your new playlist!")
        
        if choice == '3':
            print("\nHere are the possible genres to search for: ")
            gdict =  spotifyObject.recommendation_genre_seeds()

            genres = list(gdict.values())
            ugh = genres[0]

            for i in ugh:
                print(i)
            
            print()
            print("Enter up to five of the above genres, seperating by commas")
            genreChoice = input("Your choice: ")

            recs = spotifyObject.recommendations(seed_genres=[genreChoice])
            allRecs = []
            print("\nList of recommended songs based on your request:")
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_genres=[genreChoice])
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                name = input("Enter a name for the playlist: ")
                print("Please wait...")
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in allRecs:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
            
            print("Check your Spotify account for your new playlist!")
        
        if choice == '4':
            results = spotifyObject.current_user_top_tracks(5)

            songName = results['items'][0]['name']
            songID = results['items'][0]['id']

            topSongs = []

            print("\n\nYour top five songs:")
            for i, item in enumerate(results['items']):
                topSongs.append(item['artists'][0]['id'])
                print("  >>>", item['name'], ' - ', item['artists'][0]['name'])
            
            print()
            recs = spotifyObject.recommendations(seed_tracks=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
            print("List of recommended songs based on your top songs:")
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_artists=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]])
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                name = input("Enter a name for the playlist: ")
                print("Please wait...")
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in recs['tracks']:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track['id']], position=None)
            
            print("Check your Spotify account for your new playlist!")
        
        if choice == '5':
            results = spotifyObject.current_user_top_artists(limit=5)

            topArtists = []

            print("\nList of your top artists:")
            for item in results['items']:
                topArtists.append(item['id'])
                print("  >>>", item['name'])
            
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]])
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                name = input("Enter a name for the playlist: ")
                print("Please wait...")
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in recs['tracks']:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track['id']], position=None)
            
            print("Check your Spotify account for your new playlist!")
    
else:
    print()
    print("Goodbye!")
