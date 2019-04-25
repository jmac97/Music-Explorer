import spotipy
import spotipy.util as util
import config
import recom
import random

1224649854

#Initial menus options
print("\n\nWelcome to Pioneer Playlist!\n")

#Get's user's ID number
print("If you have a Facebook linked acccount, enter your Spotify ID number.")
print("If you don't know how to acquire this, see the readme.md")
print("Otherwise, enter your username.")

number = input("\nEnter your information: ")
username = number

#Create token 
token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')
print(token)

#Create Spotify object
spotifyObject = spotipy.Spotify(auth=token)
#spotifyObject.trace = False

#Get user's name
user = spotifyObject.current_user()
displayName = user['display_name']

#Print user's name
print("\n\nHi " + displayName + "!")
print("Let's create a playlist based on one of the below.\n")

while True:
    #Second menu
    print("Enter the number of one of the menu choices:")
    print("  >>> 1: Search for a song")
    print("  >>> 2. Search for an artist")
    print("  >>> 3. Search for a genre")
    print("  >>> 4. Your top songs")
    print("  >>> 5. Your top artists")
    print("  >>> 6. W I L D  C A R D")
    print("  >>> 7. Exit program\n")
    choice = input("Your choice: ")
    
    #Search for a song
    if choice == '1':
        while True:
            #Gets user's song search and searches Spotify for that name
            choice = input("Enter a name of a song: ")
            searchResults = spotifyObject.search(choice,1,0,"track")
            
            if len(searchResults['tracks']['items']) == 0:
                print("Song not found.")

            else:
                #Gets the name of the artist
                artist = searchResults['tracks']['items'][0]['artists'][0]['name']

                #Gets the song name
                song = searchResults['tracks']['items'][0]['name']
                #Gets the song ID
                songID = searchResults['tracks']['items'][0]['id']

                #Prints Name - Artist
                print("\n\nYour serarch request: " + song, ' - ', artist,"\n")

                #Gets list of song recommendations and prints the list
                allRecs = []
                recom.getRecs(songID, spotifyObject, 'song', allRecs)
            
                #Third menu 
                print("\nWould you like to make this a playlist?")
                print("Type 'Yes' to make a playlist, anyting else will pass this option.\n")
                answer = input("Your choice: ")

                if answer == 'Yes' or answer == 'yes':
                    #Names, creates, and populates playlist
                    recom.playlist(username, spotifyObject, allRecs)
                
                print("\nWould you like to generate another one or return to the main menu?")
                redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

                if redo == 'Menu' or redo == 'menu':
                    break
    
    #Search for an artist
    if choice == '2':
        while True:
            #Gets user's artist search and searches Spotify for that name
            choice = input("Enter name of an artist: ")
            searchResults = spotifyObject.search(choice,1,0,"artist")

            if len(searchResults['tracks']['items']) == 0:
                print("Artist not found.")
            
            #Gets artist base information
            artist = searchResults['artists']['items'][0]

            #Prints artist's name
            print("\n\nYour serarch request: " + artist['name'])
            #Printes the followers of the artist
            print("They have " + str(artist['followers']['total']) + " followers")
            #Lists three of the artist's styles
            print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2] + '\n')
            
            #Gets list of song recommendations and prints the list
            allRecs = []
            recom.getRecs(artist['id'], spotifyObject, 'artist', allRecs)

            #Third menu
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                #Names, creates, and populates playlist
                recom.playlist(username, spotifyObject, allRecs)
            
            print("\nWould you like to generate another one or return to the main menu?")
            redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

            if redo == 'Menu' or redo == 'menu':
                break
    
    #Search for genre
    if choice == '3':
        while True:
            #Prints list of available genres for API
            print("\nHere are the possible genres to search for: ")
            gdict =  spotifyObject.recommendation_genre_seeds()

            #Gets the genre values from dictionary
            genres = list(gdict.values())
            name = genres[0]
            names = []

            #Prints items in dictionary, aka genres
            for i in name:
                print(i)
                names.append(i)
            
            def getGenres():
                while True:
                    print("\nEnter UP TO FIVE of the above genres, seperating each by commas")
                    genreChoice = input("Your choice: ")
                    genreChoice.replace(" ", "")
                    items = genreChoice.split(',')
                    total = []

                    for x in items:
                        x.replace(",", "")
                        total.append("".join(x.split()))

                    if len(total) >= 6:
                        print("That's too many generes!")

                    else:
                        if all(x in names for x in total):
                            return genreChoice
                        else:
                            print("Genre(s) not valid, check your list.")
            
            genreChoice = getGenres()

            #Gets list of song recommendations and prints the list
            recs = spotifyObject.recommendations(seed_genres=[genreChoice], limit=100)
            allRecs = []
            print("\nList of recommended songs based on your request:")
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            #Third menu
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                #Get's name of playlist
                name = input("Enter a name for the playlist: ")
                print("Please wait...")

                #Creates playlist based on that name and populates the playlist
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in allRecs:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
            
                print("Check your Spotify account for your new playlist!")
            
            print("\nWould you like to generate another one or return to the main menu?")
            redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

            if redo == 'Menu' or redo == 'menu':
                break
    
    #Based on user's top tracks
    if choice == '4':
        while True:
            #Gets user's top five songs
            results = spotifyObject.current_user_top_tracks(5)

            #Gets song names
            songName = results['items'][0]['name']
            #Gets song IDs
            songID = results['items'][0]['id']
            topSongs = []

            #Prints song Name - Artist
            print("\n\nYour top five songs:")
            for i, item in enumerate(results['items']):
                topSongs.append(item['artists'][0]['id'])
                print("  >>>", item['name'], ' - ', item['artists'][0]['name'])
            
            print()

            #Gets list of song recommendations and prints the list
            recs = spotifyObject.recommendations(seed_tracks=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]], limit=100)
            print("List of recommended songs based on your top songs:")
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            #Third menu
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                #Get's name of playlist
                name = input("Enter a name for the playlist: ")
                print("Please wait...")

                #Creates playlist based on that name and populates the playlist
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in recs['tracks']:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track['id']], position=None)
            
                print("Check your Spotify account for your new playlist!")
            
            print("\nWould you like to generate another one or return to the main menu?")
            redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

            if redo == 'Menu' or redo == 'menu':
                break
    
    #Based on user's top artists
    if choice == '5':
        while True:
            #Gets users top 5 artists
            results = spotifyObject.current_user_top_artists(limit=5)
            topArtists = []

            #Prints and stores user's artists info
            print("\nList of your top artists:")
            for item in results['items']:
                topArtists.append(item['id'])
                print("  >>>", item['name'])
            
        #Gets list of song recommendations and prints the list
            print()
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]], limit=100)
            print("List of recommended songs based on your request:")
            for track in recs['tracks']:
                print("  >>>", track['name'], '-', track['artists'][0]['name'])

            #Third menu
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                #Get's name of playlist
                name = input("Enter a name for the playlist: ")
                print("Please wait...")

                #Creates playlist based on that name and populates the playlist
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description="Recommended Songs")
                for track in recs['tracks']:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track['id']], position=None)
            
                print("Check your Spotify account for your new playlist!")
            
            print("\nWould you like to generate another one or return to the main menu?")
            redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

            if redo == 'Menu' or redo == 'menu':
                break
    
    #W I L D  C A R D  (creates a playlist based on random genres)
    if choice == '6':
        while True:
            #Gets list of available genres for API
            gdict =  spotifyObject.recommendation_genre_seeds()

            #Gets the genre values from dictionary
            genres = list(gdict.values())
            name = genres[0]
            items = []
            x = 0

            print("\nYour playlist is made of the following random genres:")
            while x < 5:
                rando = random.choice(name)
                print("  >>> ",  rando)
                items.append(rando)
                x += 1
            
            description = 'Playlist of ' + items[0] + ', ' + items [1] + ', ' + items[3] + ', and ' + items[4]

            #Gets list of song recommendations and prints the list
            allRecs = []
            recs = spotifyObject.recommendations(seed_genres=[items[0],items[1],items[2],items[3],items[4]], limit=100)
            print("\nList of recommended songs based on your request:")
            for track in recs['tracks']:
                allRecs.append(track['id'])
                print("  >>>", track['name'], '-', track['artists'][0]['name'])
            
            #Third menu
            print("\nWould you like to make this a playlist?")
            print("Type 'Yes' or 'No'\n")
            answer = input("Your choice: ")

            if answer == 'Yes' or answer == 'yes':
                #Get's name of playlist
                name = input("Enter a name for the playlist: ")
                print("Please wait...")

                #Creates playlist based on that name and populates the playlist
                playlists = spotifyObject.user_playlist_create(username, name, public=True, description=description)
                for track in allRecs:
                    add = spotifyObject.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
            
                print("Check your Spotify account for your new playlist!")
            
            print("\nWould you like to generate another one or return to the main menu?")
            redo = input("Enter 'Menu' to return, anything else will restart this funcion: ")

            if redo == 'Menu' or redo == 'menu':
                break

    #Closes program
    if choice == '7':
        print()
        print("Goodbye!")
        break
