from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Uday Music Player")
root.geometry("920x670+290+85")
root.config(bg='#0f1a2b')
root.resizable(False,False)

mixer.init()

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

#icon
image_icon=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\top.png")
Label(root,image=Top,bg="#0f1a2b").pack()

#logo
logo=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\logo.png")
Label(root,image=logo,bg="#0f1a2b").place(x=65,y=115)

#button
play_button=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0,command=play_song).place(x=100,y=400)

stop_button=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=30,y=500)

resume_button=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=115,y=500)

pause_button=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=200,y=500)

#label
music=Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=150,y=340,anchor="center")

#music
Menu=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Music Player\\menu.png")
Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330,y=300)

scroll=Scrollbar(music_frame)
playlist = Listbox(music_frame,width=100,font=("arial",12),bg="#333333",fg="gray",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill= Y)
playlist.pack(side=LEFT,fill=BOTH)


root.mainloop()
