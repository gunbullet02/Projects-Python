from tkinter import *
From gtts import gTTS
From playsound import playsound

root = Tk()
geometry.root("350x300")
root.configure(bg = 'ghost white')
root.title("Text To Speech")

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg = 'white smoke').pack()
Label(text = "DataFlair", font = 'arial 15 bold', bg = 'white smoke', width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text = "Enter Text", font = 'arial 15 bold', bg = 'white smoke').place(x =20, y = 60)

entry_field = Entry(root, textvariable = Msg, width = '50')
entry_field.place(x = 20, y = 100)

def Text_to_speech():
    Message = entry_field.get()
    
