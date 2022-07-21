# Pioneer Playlist

## Introduction
The purpose of this project is to have users experience new music by introducing them to artists and songs. The user will input their Spotify information and then will be able to chose from a menu how they would like to generate a new playlist for them to listen to. From there, the program will generate similar songs to the inputted artist, song, genre, or from the users top songs or artists. The user will then have the oppurtunity to either turn the list of songs into a playlist or generate a new list.

This program was made using Spotipy, a python library for the Spotify Web API: https://spotipy.readthedocs.io/en/latest/#

## Steps to Take Before Running Pioneer-Playlist:
1. Have a Spotify account and know your user ID (see below if you don't know)
2. git clone the repo
3. install spotipy (pip install git+https://github.com/plamere/spotipy.git --upgrade)
4. if step 3 doesn't work, try python3 -m pip install spotipy

## What's My Spotify User ID?
The program will ask you to input your Spotify user id. If you have a Spotify account that *is* linked to Facebook, following these steps. Otherwise, you can use your actual username. There are two ways to acquire your ID number:
 You can go to this link to get your device username: https://www.spotify.com/au/account/set-device-password/
 Or:
  1. Open Spotify through the actual program, not the web player
  2. Click your username in the top right corner
  3. Click on the bubble with "..." under your name/username
  4. Click "Share"
  5. Click "Copy Profile Link"
  6. Paste this link somewhere. Your Spotify ID number is the 10 digit number after "user/"

## What's in the Examples folder?
This folder contains example snippets of the full main code. These files were used to learn how to work with the Spotify API.
