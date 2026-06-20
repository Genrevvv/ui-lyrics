import pygame
import time

from lyrics import lyrics
from tkinter import *
from window import Window

pygame.mixer.init()
pygame.mixer.music.load('castle_in_hollywood.wav')
pygame.mixer.music.play()

root = Tk()
root.withdraw()

def window0():
    window0 = Window(root, 'Castle in Hollywood', 320, 200, 0, 0)
    window0.add_text('Castle')
    window0.add_text('in')
    window0.add_text('Hollywood')
    root.after(1700, window1)

# I rack my brain
def window1():
    Window(root, 'window 1', 320, 200, -100, -150).show_lyrics(lyrics[0])
    root.after(2000, window2)

# spend hours and days
def window2():
    Window(root, 'window 2', 320, 200, -150, -200).show_lyrics(lyrics[1])
    root.after(2300, window3)

# I still can't figure it out
def window3():
    Window(root, 'window 3', 320, 200, -200, -150).show_lyrics(lyrics[2])
    root.after(3900, window4)

# what happend that year in hour house?
def window4():
    Window(root, 'window 4', 320, 200, -250, -100).show_lyrics(lyrics[3])
    root.after(3500, window5)

# still learning to live wihtout you
def window5():
    Window(root, 'window 5', 320, 200, -200, -50).show_lyrics(lyrics[4])
    root.after(4700, window6)

# I wonder what you tell your friends
def window6():
    Window(root, 'window 6', 320, 200, -150, 0).show_lyrics(lyrics[5])
    root.after(4100, window7)

# which version of our fairy story
def window7():
    Window(root, 'window 7', 320, 200, -100, 50).show_lyrics(lyrics[6])
    root.after(4000, window8)

# the one where you walk out in glory
def window8():
    Window(root, 'window 8', 320, 200, -50, 100).show_lyrics(lyrics[7])
    root.after(3500, window9)

# or the night I moved out in a hurry
def window9():
    Window(root, 'window 9', 320, 200, 0, 150).show_lyrics(lyrics[8])
    root.after(4500, window10)

# I think about you always
def window10():
    Window(root, 'window 10', 320, 200, 50, 100).show_lyrics(lyrics[9])
    root.after(3000, window11)

# tied together with a string
def window11():
    Window(root, 'window 11', 320, 200, 100, 50).show_lyrics(lyrics[10])
    root.after(2000, window12)

# I thought that lilies died by winter
def window12():
    Window(root, 'window 12', 320, 200, 150, 0).show_lyrics(lyrics[11])
    root.after(2000, window13)

# then they bloomed again in spiring
def window13():
    Window(root, 'window 13', 320, 200, 200, -50).show_lyrics(lyrics[12])
    root.after(2000, window14)

# It's a heartbreak
def window14():
    Window(root, 'window 14', 320, 200, 250, -100).show_lyrics(lyrics[13])
    root.after(2000, window15)

# marked the end of our girlhood
def window15():
    Window(root, 'window 15', 320, 200, 200, -200).show_lyrics(lyrics[14])
    root.after(2100, window16)

# we'll never go back
def window16():
    Window(root, 'window 16', 320, 200, 150, -150).show_lyrics(lyrics[15])
    root.after(1400, window17)

# to our castle in holly wood
def window17():
    Window(root, 'window 17', 320, 200, 0, 0).show_lyrics(lyrics[16])
    root.after(6000, close)

def close():
    root.destroy()
    
root.after(0, window0)
root.mainloop()
