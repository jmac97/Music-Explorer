# Pioneer Playlist
This is my EE551 Engineering Python final project

## Introduction
The purpose of this project is to have users experience new music by introducing them to artists and songs. The user will input their Spotify information and then will be able to chose from a menu how they would like to generate a new playlist for them to listen to. From there, the program will generate similar songs to the inputted artist, song, genre, or from the users top songs or artists. The user will then have the oppurtunity to either turn the list of songs into a playlist or generate a new list.

## Steps to Take Before Running Pionee-Playlist:
1. Have a Spotify account and know your user ID (see below if you don't know)
2. git clone the repo
3. install spotipy (pip install spotipy)

## What's My Spotify User ID?
The program will ask you to input your Spotify user id. To acquire this:
 1. Open Spotify
 2. Click your username in the top right corner
 3. Click on the bubble with "..." under your name/username
 4. Click "Share"
 5. Click "Copy Profile Link"
 6. Paste this link somewhere. Your Spotify ID number is the 10 digit number after "user/"

## Architecture Features (Basic Idea)
  * Interface with Spotify API
      * Log-in information
      * Scrap music information
      * Scrap user music taste information
  * Python file that stores song information
  * GUI for Spotify and playlist name information

## To Do (Basic Idea)
  * Create a user friendly GUI
  * Create an optimal front-end and back-end program
  * Get Spotify API credentials 
  * Have python program interact/connect with the Spotify API
