import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("Music Player")
music_player.resizable(0,0)
music_player.geometry("450x350")
# photo = tkr.PhotoImage(name="icon/icon.png")
# music_player.s
def open_file(event=None):
    global play_list,directory
    directory = askdirectory()    
    os.chdir(directory)
    song_list = os.listdir()
    play_list = tkr.Listbox(music_player,justify='right',font="Helvetica 12 bold",bg="black",fg="white",selectmode=tkr.SINGLE)
    for item in song_list:
        a = 0
        play_list.insert(a,item)
        a+=1
    play_list.pack(fill='x', expand="yes")
def exit_app(event=None):
    music_player.destroy()
    print("Exiting...")
    quit()
    
main_menu = tkr.Menu(music_player)
music_player.config(menu=main_menu)
filemenu = tkr.Menu(main_menu)
filemenu.add_command(label="Open File",accelerator="Ctrl+O",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit",accelerator="Ctrl+Q",command=exit_app)
main_menu.add_cascade(label="File",menu=filemenu)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
# play_list.pack(fill="both", expand="yes")

music_player.bind("<Control-o>",open_file)
music_player.bind("<Control-q>",exit_app)
music_player.mainloop()
