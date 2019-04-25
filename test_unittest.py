import unittest
from unittest.mock import patch
import Pioneer_Playlist
from Pioneer_Playlist import search
from Pioneer_Playlist import getRecs
from Pioneer_Playlist import printRecs
from Pioneer_Playlist import playlist
from Pioneer_Playlist import getGenres
import spotipy
import spotipy.util as util
import config


class Test_search(unittest.TestCase):

    def setUp(self):
        self.token = util.prompt_for_user_token('1224649854', scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')
        self.spotifyObject = spotipy.Spotify(auth=self.token)
    
    #Tests that a song is correctly searched for and retrieved
    @patch('Pioneer_Playlist.input', return_value='Heat Wave')
    def test_search_for_song(self, input):
        self.search = search(self.spotifyObject, 'track')
        self.song = self.search['tracks']['items'][0]['name']
        
        self.assertEqual('Heat Wave', self.song)
    
    #Tests that an artist is correctly searched for and retrieved
    @patch('Pioneer_Playlist.input', return_value='Snail Mail')
    def test_search_for_artist(self, input):
        self.search = search(self.spotifyObject, 'artist')
        self.artist = self.search['artists']['items'][0]['name']
        
        self.assertEqual('Snail Mail', self.artist)


class Test_getRecs(unittest.TestCase):

    def setUp(self):
        self.token = util.prompt_for_user_token('1224649854', scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')
        self.spotifyObject = spotipy.Spotify(auth=self.token)
        
        self.recList = []
        
    #Tests if a song is searched
    def test_song(self):
        #Uses the song Heat Wave's song ID
        self.song = getRecs('43E0f1S0rOGCo6YYRYHjHP', self.spotifyObject, 'song', self.recList)
        self.assertTrue(self.song)
    
    #Tests if an artist is searched
    def test_artist(self):
        #Uses the artist Snail Mail's ID
        self.artist = getRecs('4QkSD9TRUnMtI8Fq1jXJJe', self.spotifyObject, 'song', self.recList)
        self.assertTrue(self.artist)
    
    #Tests if a genre is searched
    def test_genre(self):
        #Uses the genre punk's ID
        self.genre = getRecs('punk', self.spotifyObject, 'genre', self.recList)
        self.assertTrue(self.genre)
    
    #Tests is a playlist of 100 songs is made
    def test_amount(self):
        #Uses the song Heat Wave's song ID
        self.song = getRecs('43E0f1S0rOGCo6YYRYHjHP', self.spotifyObject, 'song', self.recList)
        self.assertEqual(100, len(self.recList))
    
    #Tests to see if track IDs are being stored
    def test_ID(self):
        #Uses the song Heat Wave's song ID
        self.song = getRecs('43E0f1S0rOGCo6YYRYHjHP', self.spotifyObject, 'song', self.recList)

        for x in self.recList:
            self.assertEqual(22, len(x))


class Test_playlist(unittest.TestCase):

    def setUp(self):
        self.username = '1224649854'
        self.token = util.prompt_for_user_token('1224649854', scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')
        self.spotifyObject = spotipy.Spotify(auth=self.token)

        self.items = []
    
    #Tests if 'Yes' will make a playlist
    @patch('Pioneer_Playlist.input', return_value = 'Yes')
    def test_input_Cap(self, input):
        self.playlist = playlist(self.username, self.spotifyObject, self.items)

        self.assertTrue(self.playlist)
    
    #Tests if 'yes' will make a playlist
    @patch('Pioneer_Playlist.input', return_value = 'Yes')
    def test_input_noCap(self, input):
        self.playlist = playlist(self.username, self.spotifyObject, self.items)

        self.assertTrue(self.playlist)
    
    #Tests if anything else will leave function
    @patch('Pioneer_Playlist.input', return_value = 'aeirnd')
    def test_input_no_playlist(self, input):
        self.playlist = playlist(self.username, self.spotifyObject, self.items)

        self.assertFalse(self.playlist)

class Test_getGenres(unittest.TestCase):

    def setUp(self):
        self.token = util.prompt_for_user_token('1224649854', scope='playlist-modify-private,playlist-modify-public,user-top-read', client_id=config.cID,client_secret=config.cSecret,redirect_uri='https://www.google.com/')
        self.spotifyObject = spotipy.Spotify(auth=self.token)

        self.gdict = self.spotifyObject.recommendation_genre_seeds()
        self.genres = (list(self.gdict.values()))[0]
        self.names = []

        for i in self.genres:
            self.names.append(i)
    
    #Tests if genre will be returned
    @patch('Pioneer_Playlist.input', return_value = 'sad')
    def test_input(self, input):
        self.genre = getGenres(self.names)

        self.assertEqual(self.genre, "sad")
    
    #Tests if too many genres have been inputted
    @patch('Pioneer_Playlist.input', return_value = 'sad, sad, sad, sad, sad, sad')
    def test_input_amount(self, input):
        self.assertEqual(1, getGenres(self.names))
    
    #Tests if an invalid genre is inputted
    @patch('Pioneer_Playlist.input', return_value = 'this is not a genre')
    def test_input_valid(self, input):
        self.assertEqual(2, getGenres(self.names))

if __name__ == '__main__':
    unittest.main()
