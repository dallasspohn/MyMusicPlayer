# importing libraries
import os
import random
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background="#212121")
root.resizable(False, False)
mixer.init()

# Global variables
songs = []  # List to store the songs
current_song_index = 0  # Index of the currently playing song

# Create a function to open a file
def AddMusic():
    global songs
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir()
        songs = [song for song in songs if song.endswith(".mp3")]  # Filter only MP3 files
        Playlist.delete(0, END)  # Clear the existing playlist
        for song in songs:
            Playlist.insert(END, song)

def PlayMusic():
    global current_song_index
    if len(songs) == 0:
        return
    song = songs[current_song_index]
    mixer.music.load(song)
    mixer.music.play()

def NextTrack():
    global current_song_index
    if len(songs) == 0:
        return
    current_song_index = (current_song_index + 1) % len(songs)
    PlayMusic()

def PrevTrack():
    global current_song_index
    if len(songs) == 0:
        return
    current_song_index = (current_song_index - 1) % len(songs)
    PlayMusic()

# Rest of the code...

# Button for playing the next track
ButtonNext = PhotoImage(file="next.png")
Button(root, image=ButtonNext, bg="#0f1a2b", bd=0, command=NextTrack).place(
    x=300, y=400
)

# Button for playing the previous track
ButtonPrev = PhotoImage(file="previous.png")
Button(root, image=ButtonPrev, bg="#0f1a2b", bd=0, command=PrevTrack).place(
    x=400, y=400
)

# Rest of the code...

# Execute Tkinter
root.mainloop()