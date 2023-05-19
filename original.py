import tkinter
import pygame
import os
from tkinter import Listbox,Menu,Button,Frame,PhotoImage,messagebox,filedialog

dictsongs = {}

def play():
    root.title("OS mp3 Player")
    name = listsongs.get(tkinter.ACTIVE)

    if current.get()==name:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            pausePlayBtn.configure(image=listDirBtnImg)
            return
        else:
            pygame.mixer.music.unpause()
            pausePlayBtn.configure(image=pausePlayBtnImg)
            return

    try:
        pygame.mixer.music.load(dictsongs[name])
    except Exception as e:
        if isinstance(e,pygame.error): 
            root.title(f"OS mp3 Player [Corrupt file: Could not play]")
            return
        else:
            raise e

    current.set(name) 
    var.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()


def showMentor():
    messagebox.showinfo("OUR MENTOR", "Dr. Manikandan V M")

def showContributors():
    messagebox.showinfo("CONTRIBUTORS", "Tanishk Yadav\nSanjana Maini")

def addSong():
    initDirectory = filedialog.askdirectory()
    music_formats = [
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".ogg",
        ".wma",
        ".m4a",
        ".alac",
        ".aiff",
        ".opus",
    ]
    for drive in initDirectory:
        for root, dirs, files in os.walk(initDirectory):
            for file in files:
                for format in music_formats:
                    if file.endswith(format):
                        file = file.replace(initDirectory, '')
                        dictsongs[file.replace(format, '')] = os.path.join(root, file)
                        listsongs.insert(tkinter.END, file.replace(format, ''))




root = tkinter.Tk()
root.title("OS mp3 Player")
root.geometry("450x450")

pygame.mixer.init()

var = tkinter.StringVar()
current = tkinter.StringVar()
var.set("Select the song to play")

listsongs = Listbox(root, bg='red', width=55)
for song_name, path in dictsongs.items():
    listsongs.insert(0, song_name)

listsongs.pack(pady=4)

listDirBtnImg = PhotoImage(file='Icons1/list.png')
prevBtnImg = PhotoImage(file='Icons1/previous.png')
fwdBtnImg = PhotoImage(file='Icons1/next-button.png')
pausePlayBtnImg = PhotoImage(file='Icons1/pause.png')

controllersFrame = Frame(root)
controllersFrame.pack()

listDirBtn = Button(controllersFrame, image=listDirBtnImg, borderwidth=0)
prevBtn = Button(controllersFrame, image=prevBtnImg, borderwidth=0)
fwdBtn = Button(controllersFrame, image=fwdBtnImg, borderwidth=0)
pausePlayBtn = Button(controllersFrame, image=pausePlayBtnImg, borderwidth=0, command=play)

listDirBtn.grid(row=0, column=0, padx=15)
prevBtn.grid(row=0, column=1, padx=15)
fwdBtn.grid(row=0, column=3, padx=15)
pausePlayBtn.grid(row=0, column=2, padx=15)

playermenu = Menu(root)
root.config(menu=playermenu)

MixMenu = Menu(playermenu)
playermenu.add_cascade(label="Credits", menu=MixMenu)
MixMenu.add_command(label="Mentor", command=showMentor)
MixMenu.add_command(label="Contributors", command=showContributors)
playermenu.add_command(label="Start Search", command=addSong)

root.mainloop()
