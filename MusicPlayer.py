import os
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter import filedialog
root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []
index = 0
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    update()


def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    update()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def update():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def directorychooser():
    directory = filedialog.askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdic = os.path.realpath(files)
            audio = ID3(realdic)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()

label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()
#listofsongs.reverse()
realnames.reverse()
for items in realnames:
    listbox.insert(0, items)


realnames.reverse()
#listofsongs.reverse()
nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

stopbutton = Button(root, text='stop music')
stopbutton.pack()

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()

