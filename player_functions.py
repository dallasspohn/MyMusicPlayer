import os
import random
import time
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer



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
    pygame.mixer.music.load(Playlist.get(ACTIVE))
    pygame.mixer.music.play()

# def ShuffleMusic():
#     global songs
#     for song in songs:
#         Music_Shuffle = random.choice(songs)
#         if song == "System Volume Information":
#             continue
#         if song == "FOUND.000":
#             continue
#         print(Music_Shuffle[0:-4])
#         pygame.mixer.music.load(Music_Shuffle)
#         pygame.mixer.music.play()
#         pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Register end event
#         pygame.event.wait()  # Wait for the end event

# def ShuffleMusic():
#     global songs
#     for song in songs:
#         Music_Shuffle = random.choice(songs)
#         if song == "System Volume Information":
#             continue
#         if song == "FOUND.000":
#             continue
#         print(Music_Shuffle[0:-4])
#         pygame.mixer.music.load(Music_Shuffle)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             time.sleep(1)  # Add a short delay between each check

# def ShuffleMusic():
#     global songs
#     for song in songs:
#         Music_Shuffle = random.choice(songs)
#         if song == "System Volume Information":
#             continue
#         if song == "FOUND.000":
#             continue
#         print(Music_Shuffle[0:-4])
#         pygame.mixer.music.load(Music_Shuffle)
#         pygame.mixer.music.play()
#         end_event = pygame.USEREVENT + 1
#         pygame.mixer.music.set_endevent(end_event)
#         event_triggered = False
#         while not event_triggered:
#             for event in pygame.event.get():
#                 if event.type == end_event:
#                     event_triggered = True
#                     break
#             time.sleep(0.1)

def ShuffleMusic():
    global songs
    for song in songs:
        Music_Shuffle = random.choice(songs)
        if song == "System Volume Information":
            continue
        if song == "FOUND.000":
            continue
        try:
            print(Music_Shuffle[0:-4])
            mixer.music.load(Music_Shuffle)
            mixer.music.play()
            end_event = pygame.USEREVENT + 1
            mixer.music.set_endevent(end_event)
            event_triggered = False
            while not event_triggered:
                for event in pygame.event.get():
                    if event.type == end_event:
                        event_triggered = True
                        break
                time.sleep(0.1)
        except (pygame.error, FileNotFoundError) as e:
            print(f"Error loading audio file: {Music_Shuffle}")
            print(str(e))

# def ShuffleMusic():
#     global songs
#     while True:
#         Music_Shuffle = random.choice(songs)
#         if Music_Shuffle == "System Volume Information" or Music_Shuffle == "FOUND.000":
#             continue
#         try:
#             print(Music_Shuffle[0:-4])
#             mixer.music.load(Music_Shuffle)
#             mixer.music.play()
#             end_event = pygame.USEREVENT + 1
#             mixer.music.set_endevent(end_event)
#             event_triggered = False
#             while not event_triggered:
#                 for event in pygame.event.get():
#                     if event.type == end_event:
#                         event_triggered = True
#                         break
#                 time.sleep(0.1)
#             break # Exit the loop after the first song is played
#         except (pygame.error, FileNotFoundError) as e:
#             print(f"Error loading audio file: {Music_Shuffle}")
#             print(str(e))

def ForwardTrack():
    current_index = Playlist.curselection()
    if current_index:
        next_index = current_index[0] + 1
        if next_index < Playlist.size():
            Playlist.selection_clear(0, END)
            Playlist.selection_set(next_index)
            PlayMusic()

def ReverseTrack():
    current_index = Playlist.curselection()
    if current_index:
        prev_index = current_index[0] - 1
        if prev_index >= 0:
            Playlist.selection_clear(0, END)
            Playlist.selection_set(prev_index)
            PlayMusic()

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

# # Entry point of the program
# if __name__ == "__main__":
