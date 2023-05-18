from tkinter import *
import pygame
import os
from tkinter import messagebox
from tkinter import filedialog

dictsongs={}

def play():
    song=listsongs.get(ACTIVE)


def showMentor():
    messagebox.showinfo("OUR MENTOR","Dr. Manikandan V M ")

def showContributors():
    messagebox.showinfo("CONTRIBUTORS","Tanishk Yadav\nSanjana Maini")

def addSong():
    initDirectory=filedialog.askdirectory()
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

    dictsongs = dict()
    for drive in initDirectory:
        for root, dirs, files in os.walk(initDirectory):
            for file in files:
                for format in music_formats:
                    if file.endswith(format):
                        file=file.replace(initDirectory,'')
                        file=file.replace(format,'')
                        listsongs.insert(file)
                        dictsongs[file] = os.path.join(root, file)


root=Tk()
root.title("OS mp3 Player")
root.geometry("450x750")

pygame.mixer.init()

listsongs=[]
for key in dictsongs:
    listsongs.insert('{}\t\t{}'.format(key,dictsongs[key]))

listsongs=Listbox(root,bg='red',width=55 )
    
listsongs.pack(pady=4)

listDirBtnImg=PhotoImage(file='Downloads/Icons1/list.png')
# listDirBtnImg.zoom(60,60)
prevBtnImg=PhotoImage(file='Downloads/Icons1/previous.png')
fwdBtnImg=PhotoImage(file='Downloads/Icons1/next-button.png')
pausePlayBtnImg=PhotoImage(file='Downloads/Icons1/pause.png')
# playBtnImg=PhotoImage(file='Downloads/Icons1/play-button.png')
# pauseBtnImg=PhotoImage(file='Downloads/Icons1/pause-button.png')

controllersFrame=Frame(root)
controllersFrame.pack()

listDirBtn=Button(controllersFrame,image=listDirBtnImg,borderwidth=0,command=play)
prevBtn=Button(controllersFrame,image=prevBtnImg,borderwidth=0)
fwdBtn=Button(controllersFrame,image=fwdBtnImg,borderwidth=0)
pausePlayBtn=Button(controllersFrame,image=pausePlayBtnImg,borderwidth=0)
# playBtn=Button(controllersFrame,image=playBtnImg,borderwidth=0)
# pauseBtn=Button(controllersFrame,image=pauseBtnImg,borderwidth=0)

listDirBtn.grid(row=0,column=0,padx=15)
prevBtn.grid(row=0,column=1,padx=15)
fwdBtn.grid(row=0,column=3,padx=15)
pausePlayBtn.grid(row=0,column=2,padx=15)
# playBtn.grid(row=0,column=4,padx=10)
# pauseBtn.grid(row=0,column=5,padx=10)

playermenu=Menu(root)
root.config(menu=playermenu)

MixMenu=Menu(playermenu)
playermenu.add_cascade(label="Credits",menu=MixMenu)
MixMenu.add_command(label="Mentor",command=showMentor)
MixMenu.add_command(label="Contributors",command=showContributors)
playermenu.add_command(label="Start Search",command=addSong)






root.mainloop()