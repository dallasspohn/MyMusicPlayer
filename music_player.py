import os
import random
import time
from tkinter import filedialog, END, ACTIVE  # Add ACTIVE to the import statement
import pygame
from pygame import mixer

def AddMusic(playlist):
    global songs
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir()
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)
        return songs


def PlayMusic(playlist):
    Music_Name = playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()


def ShuffleMusic(playlist):
    global songs
    for song in songs:
        Music_Shuffle = random.choice(songs)
        if song == "System Volume Information":
            continue
        if song == "FOUND.000":
            continue
        try:
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
            break
        except (pygame.error, FileNotFoundError) as e:
            print(Music_Shuffle)


def ForwardTrack(playlist):
    current_index = playlist.curselection()
    if current_index:
        next_index = current_index[0] + 1
        if next_index < playlist.size():
            playlist.selection_clear(0, END)
            playlist.selection_set(next_index)
            PlayMusic(playlist)


def ReverseTrack(playlist):
    current_index = playlist.curselection()
    if current_index:
        prev_index = current_index[0] - 1
        if prev_index >= 0:
            playlist.selection_clear(0, END)
            playlist.selection_set(prev_index)
            PlayMusic(playlist)