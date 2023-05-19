import tkinter
import pygame
import os
from tkinter import Listbox,Menu,Button,Frame,PhotoImage,messagebox,filedialog

dictsongs = {}

def play():
    pausePlayBtn.configure(image=pausePlayBtnImg)
    root.title("OS mp3 Player")
    name = listsongs.get(tkinter.ACTIVE)

    if current.get()==name:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            pausePlayBtn.configure(image=pauseImg)
            return
        else:
            pygame.mixer.music.unpause()
            pausePlayBtn.configure(image=playImg)
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
    messagebox.

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
root.geometry("350x450")
root.configure(bg='black')

pygame.mixer.init()

var = tkinter.StringVar()
current = tkinter.StringVar()
var.set("Select the song to play")

listsongs = Listbox(root, bg='red', width=40,height=18)
for song_name, path in dictsongs.items():
    listsongs.insert(0, song_name)

listsongs.pack(pady=4)

prevBtnImg = PhotoImage(file='Icons1/previous.png')
pauseImg = PhotoImage(file='Icons1/pause.png')
playImg = PhotoImage(file='Icons1/play.png')
fwdBtnImg = PhotoImage(file='Icons1/next-button.png')
pausePlayBtnImg = PhotoImage(file='Icons1/playpause.png')

controllersFrame = Frame(root,bg='white')
controllersFrame.pack()

listDirBtn = Button(controllersFrame, image=pausePlayBtnImg, borderwidth=0,bg='white')
prevBtn = Button(controllersFrame, image=prevBtnImg, borderwidth=0,bg='white')
fwdBtn = Button(controllersFrame, image=fwdBtnImg, borderwidth=0,bg='white')
pausePlayBtn = Button(controllersFrame, image=pausePlayBtnImg, borderwidth=0, command=play,bg='white')

prevBtn.grid(row=0, column=0, padx=18)
fwdBtn.grid(row=0, column=2, padx=18)
pausePlayBtn.grid(row=0, column=1, padx=18)

playermenu = Menu(root,bg='white')
root.config(menu=playermenu)

MixMenu = Menu(playermenu)
playermenu.add_cascade(label="Credits", menu=MixMenu)
MixMenu.add_command(label="Mentor", command=showMentor)
MixMenu.add_command(label="Contributors", command=showContributors)
playermenu.add_command(label="Start Search", command=addSong)

root.mainloop()