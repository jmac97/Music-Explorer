import spotipy
import spotipy.util as util
import config
import random

#Gets and returns search results
##object: Spotify object
##type: What is the user searching for e.g. song, artist, etc? Options: track, artist
def search(object, type):
    choice = input("Search for something: ")
    searchResults = object.search(choice, 1, 0, type)

    return searchResults


#Prints song Name - Artist, returns list of track id numbers
##list: list of song info
##total: empty list that function will dump song ids into
def printRecs(list, total):
    print("\nList of recommended songs based on your request:")
    for track in list['tracks']:
        total.append(track['id'])
        print("  >>>", track['name'], '-', track['artists'][0]['name'])

    return total


#Gets recommendations based on inputs
##item: ID of thing that will be used to base the recommendation on
##sp: Spotify object
##type: What kind of item is the user looking to get a recommendation on? Can be song, artist, or genre
##list: empty list for printRecs function, see above
def getRecs(item, sp, type, list):
    recs = []

    #Gets recommendations from songs
    if type == 'song':
        recs = sp.recommendations(seed_tracks=[item], limit=100)
        printRecs(recs, list)
        return True

    #Gets recommendations from artists
    if type == 'artist':
        recs = sp.recommendations(seed_artists=[item], limit=100)
        printRecs(recs, list)
        return True

    #Gets recommendations from genres
    if type == 'genre':
        recs = sp.recommendations(seed_genres=[item], limit=100)
        printRecs(recs, list)
        return True
    

#Creates and populates a playlist
##username: username/ID of user
##sp: Spotify object
##list: list of track IDs
def playlist(username, sp, list):
    print("\nWould you like to make this a playlist?")
    print("Type 'Yes' to make a playlist, anyting else will pass this option.\n")
    answer = input("Your choice: ")

    if answer == 'Yes' or answer == 'yes':
        name = input("Enter a name for the playlist: ")
        print("Please wait...")

        #Creates playlist based on that name and populates the playlist
        playlists = sp.user_playlist_create(username, name, public=True, description="Recommended Songs")
        for track in list:
            add = sp.user_playlist_add_tracks(username, playlists['id'], [track], position=None)
        
        print("Check your Spotify account for your new playlist!")
        return True
    
    else:
        return False


#Gets and prints list of all possible genres, returns list of genres that user chose
##list: list of all genre seeds
def getGenres(list):
    while True:
        print("\nEnter UP TO FIVE of the above genres, seperating each by commas")
        genreChoice = input("Your choice: ")

        genreChoice.replace(" ", "")
        items = genreChoice.split(',')
        total = []

        for x in items:
            x.replace(",", "")
            total.append("".join(x.split()))

        #Sees if user inputted too many genres
        if len(total) >= 6:
            print("That's too many generes!")
            return 1

        #Sees if user inputted genre(s) is within the list of available genres
        else:
            if all(x in list for x in total):
                return genreChoice
            else:
                print("Genre(s) not valid, check your list.")
                return 2


#Class that acquires user information
class userInfo:

    #Initial instructions
    def __init__(self):
        print("\n\nWelcome to Pioneer Playlist!\n")
        print("If you have a Facebook linked acccount, enter your Spotify ID number.")
        print("If you don't know how to acquire this, see the readme.md")
        print("Otherwise, enter your username.")

        #Gets user's information
        self.ID = input("\nEnter your information: ")
    
    #Returns user's information, needed for other functions
    def acquireUsername(self):
        username = self.ID
        return username

    #Creates token and a Spotify object, returns the Spotify object
    def acquireToken(self):
        username = self.acquireUsername()

        #Create token 
        token = util.prompt_for_user_token(username, scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')

        #Create Spotify object
        spotifyObject = spotipy.Spotify(auth=token)
        spotifyObject.trace = False

        #Get user's name
        user = spotifyObject.current_user()
        displayName = user['display_name']

        #Print user's name
        print("\n\nHi " + displayName + "!")
        return spotifyObject


#Class for functions within the main menu
class MainMenu:
    
    #Setup
    ##username: username/ID
    ##object: Spotify object
    def __init__(self, username, obj):
        print("Enter the number of one of the menu choices:")
        print("  >>> 1: Search for a song")
        print("  >>> 2. Search for an artist")
        print("  >>> 3. Search for a genre")
        print("  >>> 4. Your top songs")
        print("  >>> 5. Your top artists")
        print("  >>> 6. W I L D  C A R D")
        print("  >>> 7. Exit program\n")
        
        self.choice = input("Your choice: ")
        self.username = username
        self.obj = obj
    
    #Option One: "Search for a song"
    #Has user search for a song name and prints the result, returns the song's ID number
    def optionOne(self):
        if self.choice != '1':
            return 0

        while True:
            searchResults = search(self.obj, 'track')
            
            #Sees if song is on Spotify
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
                return songID
    
    #Option Two: "Search for an artist"
    #Has user search for an artist and prints the result and some information on the artist, returns the artist's ID number
    def optionTwo(self):
        if self.choice != '2':
            return 0
        
        while True:
            searchResults = search(self.obj, 'artist')

            #Sees if artist is on Spotify
            if len(searchResults['artists']['items']) == 0:
                print("Artist not found.")
            
            else:
                #Gets artist base information
                artist = searchResults['artists']['items'][0]
                #Gets artit's ID number
                artistID = artist['id']

                #Prints artist's name
                print("\n\nYour serarch request: " + artist['name'])
                #Prints the followers of the artist
                print("They have " + str(artist['followers']['total']) + " followers")
                #Lists three of the artist's styles
                print("Their styles are: " + artist['genres'][0] + ", " + artist['genres'][1] + ", and " + artist['genres'][2] + '\n')
                
                return artistID
    
    #Option Three: "Search for a genre"
    #Has the user pick from a list of genres, returns their choices
    def optionThree(self):
        if self.choice != '3':
            return 0
        
        while True:
            #Prints list of available genres for API
            print("\nHere are the possible genres to search for: ")
            gdict =  spotifyObject.recommendation_genre_seeds()

            #Gets the genre values from dictionary
            genres = list(gdict.values())
            name = genres[0]
            names = []

            #Prints items in the dictionary, aka genres
            for i in name:
                print(i)
                names.append(i)
            
            genreChoice = getGenres(names)

            #Added for unittest
            while genreChoice == 1 or genreChoice == 2:
                genreChoice = getGenres(names)

            return genreChoice
    
    #Option Four: "Your top songs"
    #Gets and prints the users top five songs and returns their ID number
    def optionFour(self):
        if self.choice != '4':
            return 0
        
        while True:
            #Gets user's top five songs
            results = spotifyObject.current_user_top_tracks(5)

            topSongs = []

            #Prints song Name - Artist
            print("\n\nYour top five songs:")
            for i, item in enumerate(results['items']):
                topSongs.append(item['id'])
                print("  >>>", item['name'], ' - ', item['artists'][0]['name'])
            
            return topSongs

    #Option Five: "Your top artists"
    #Gets and prints the users top five artists and returns their ID number
    def optionFive(self):
        if self.choice != '5':
            return 0 
        
        while True:
             #Gets users top 5 artists
            results = spotifyObject.current_user_top_artists(limit=5)
            topArtists = []

            #Prints and stores user's artists info
            print("\nList of your top artists:")
            for item in results['items']:
                topArtists.append(item['id'])
                print("  >>>", item['name'])
            
            return topArtists
    
    #Option Six: "W I L D  C A R D"
    #Takes five random genres from all available genres and returns their IDs
    def optionSix(self):
        if self.choice != '6':
            return 0
        
        while True:
            #Gets list of available genres for API
            gdict =  spotifyObject.recommendation_genre_seeds()

            #Gets the genre values from dictionary
            genres = list(gdict.values())
            name = genres[0]
            names = []
            counter = 0

            print("\nYour playlist is made of the following random genres:")
            while counter < 5:
                #Gets five random genres and prints them
                rando = random.choice(name)
                print("  >>> ",  rando)
                #Adds them to list
                names.append(rando)
                counter += 1

            return names
    
    #Option Seven: "Exit program"
    #Returns 1
    def optionSeven(self):
        if self.choice != '7':
            return 0
        
        return 1

#Main function
if __name__ == "__main__":

    #Gets user information
    user = userInfo()
    username = user.acquireUsername()
    spotifyObject = user.acquireToken()

    while True:
        print("\nLet's create a playlist based on one of the options below.\n")
        
        #Gets menu options
        menu = MainMenu(username, spotifyObject)

        #Gets user's input
        song = menu.optionOne()
        artist = menu.optionTwo()
        genre = menu.optionThree()
        topSongs = menu.optionFour()
        topArtists = menu.optionFive()
        wildCard = menu.optionSix()
        leave = menu.optionSeven()

        #If option one was chosen:
        if song != 0:
            allRecs = []
            getRecs(song, spotifyObject, 'song', allRecs)
        
        #If option two was chosen:
        if artist != 0:
            allRecs = []
            getRecs(artist, spotifyObject, 'artist', allRecs)
        
        #If option three was chosen:
        if genre != 0:
            allRecs = []
            getRecs(genre, spotifyObject, 'genre', allRecs)
        
        #If option four was chosen:
        if topSongs != 0:
            allRecs = []
            recs = spotifyObject.recommendations(seed_tracks=[topSongs[0],topSongs[1],topSongs[2],topSongs[3],topSongs[4]], limit=100)
            printRecs(recs, allRecs)
        
        #If option five was chosen:
        if topArtists != 0:
            allRecs = []
            recs = spotifyObject.recommendations(seed_artists=[topArtists[0],topArtists[1],topArtists[2],topArtists[3],topArtists[4]], limit=100)
            printRecs(recs, allRecs)

        #If option six was chosen:
        if wildCard != 0:
            allRecs = []
            description = 'Playlist of ' + wildCard[0] + ', ' + wildCard[1] + ', ' + wildCard[3] + ', and ' + wildCard[4]
            recs = spotifyObject.recommendations(seed_genres=[wildCard[0],wildCard[1],wildCard[2],wildCard[3],wildCard[4]], limit=100, description=description)
            printRecs(recs, allRecs)
        
        #If option seven was chosen:
        if leave != 0:
            print("\nGoodbye!")
            break
        
        #Generates playlist
        playlist(username, spotifyObject, allRecs)
