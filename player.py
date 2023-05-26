# importing libraries
import os
import random
import time
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import pygame
from pygame import mixer

#playlist="F:\"

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background="#212121")
root.resizable(False, False)



mixer.init()


# Create a function to open a file
def AddMusic():
    global songs
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir()
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
#        print(songs)
        return songs


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

## Shuffle is good but makes windows busy.
# def ShuffleMusic():
#     global songs
#     for song in songs:

#         Music_Shuffle = random.choice(songs)
#         if song == "System Volume Information":
#             continue
#         if song == "FOUND.000":
#             continue
#         print(Music_Shuffle[0:-4])
#         mixer.music.load(Music_Shuffle)
#         mixer.music.play()
#         while mixer.music.get_busy():
#             pass

# Shuffle from ChatGPT
# def ShuffleMusic():
#     global songs
#     for song in songs:
#         Music_Shuffle = random.choice(songs)
#         if song == "System Volume Information":
#             continue
#         if song == "FOUND.000":
#             continue
#         print(Music_Shuffle[0:-4])
#         mixer.music.load(Music_Shuffle)
#         mixer.music.play()
#         while mixer.music.get_busy():
#             time.sleep(1)  # Add a short delay between each check

def ShuffleMusic():
    global songs
    for song in songs:
        Music_Shuffle = random.choice(songs)
        if song == "System Volume Information":
            continue
        if song == "FOUND.000":
            continue
        print(Music_Shuffle[0:-4])
        mixer.music.load(Music_Shuffle)
        mixer.music.play()
        mixer.music.set_endevent(pygame.USEREVENT)  # Register end event
        pygame.event.wait()  # Wait for the end event


# icon
image_icon = PhotoImage(file="image.png")
root.iconphoto(False, image_icon)
Top = PhotoImage(file="background.png")
Label(root, image=Top, bg="#0f1a2b").pack()

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#0f1a2b", bd=0).place(x=10, y=20)


# Button
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0, command=PlayMusic).place(
    x=100, y=400
)
ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(
    x=30, y=500
)
ButtonResume = PhotoImage(file="resume.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(
    x=115, y=500
)
ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(
    x=200, y=500
)

ButtonShuffle = PhotoImage(file="shuffle.png")
Button(root, image=ButtonShuffle, bg="#0f1a2b", bd=0, command=ShuffleMusic).place(
    x=200, y=400
)


# Label Choose mp3
Menu = PhotoImage(file="background.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=LEFT)
Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)
Button(
    root,
    text="Open Folder",
    width=15,
    height=2,
    font=("times new roman", 12, "bold"),
    fg="Black",
    bg="#21b3de",
    command=AddMusic,
).place(x=330, y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(
    Frame_Music,
    width=100,
    font=("Times new roman", 10),
    bg="#333333",
    fg="grey",
    selectbackground="lightblue",
    cursor="hand2",
    bd=0,
    yscrollcommand=Scroll.set,
)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)


# Execute Tkinter
root.mainloop()