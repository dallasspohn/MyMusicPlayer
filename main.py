# importing libraries
import os
import random
import time
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import pygame
from pygame import mixer
from music_player import AddMusic, PlayMusic, ShuffleMusic, ForwardTrack, ReverseTrack

log = "playlog.txt"

# Create a GUI window
root = Tk()
root.title("Music Player")
root.geometry("920x600+290+85")
root.configure(background="#212121")
root.resizable(False, False)
root.bind("<Right>", lambda event: ForwardTrack(Playlist))
root.bind("<Left>", lambda event: ReverseTrack(Playlist))

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

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
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0, command=lambda: PlayMusic(Playlist)).place(x=100, y=400)
ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd=0, command=pygame.mixer.music.stop).place(x=30, y=500)
ButtonResume = PhotoImage(file="resume.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0, command=pygame.mixer.music.unpause).place(x=115, y=500)
ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0, command=pygame.mixer.music.pause).place(x=200, y=500)

ButtonShuffle = PhotoImage(file="shuffle.png")
Button(root, image=ButtonShuffle, bg="#0f1a2b", bd=0, command=lambda: ShuffleMusic(Playlist)).place(x=200, y=400)

# Stash for now.
# ButtonForward = PhotoImage(file="forward.png")
# Button(root, image=ButtonForward, bg="#0f1a2b", bd=0, command=lambda: ForwardTrack(Playlist)).place(x=285, y=500)

# ButtonReverse = PhotoImage(file="reverse.png")
# Button(root, image=ButtonReverse, bg="#0f1a2b", bd=0, command=lambda: ReverseTrack(Playlist)).place(x=40, y=500)

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
    command=lambda: AddMusic(Playlist)
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