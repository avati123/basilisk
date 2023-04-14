import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk


root=Tk()

style = font.Font(size=25)
style2 = font.Font(size=30)
mainMenu = Frame(root)
readRFID = Frame(mainMenu)
writeRFID = Frame(mainMenu)
wifiattacks  = Frame(mainMenu)
background  = Frame(mainMenu)

mainMenu.grid(row=0, column=0, sticky="nsew")
readRFID.grid(row=0, column=0,sticky="nsew")
writeRFID.grid(row=0, column=0, sticky="nsew")
wifiattacks.grid(row=0, column=0, sticky="nsew")
background.grid(row=0, column=0, sticky="nsew")


mainMenu.tkraise()

readRFIDlabel = Label(readRFID, text='Page 1', font=style)
readRFIDlabel.place(x=10, y=40)
writeRFIDlabel = Label(writeRFID, text='Page 2', font=style)
wifiattackslabel = Label(wifiattacks, text='Page 3', font=style)
backgroundlabel = Label(background, font=style, text=' ')
readRFIDlabel.pack(pady=230, padx=120)
writeRFIDlabel.pack(pady=230, padx=120)
wifiattackslabel.pack(pady=230, padx=120)
backgroundlabel.pack(pady=230, padx=120)








lblrr=Button(mainMenu, text="🂡 Read RFID",  fg='blue', bg= 'red',highlightbackground='black', command=lambda: readRFID.tkraise() ,font=("Helvetica", 16), width=27)
lblrr.place(x=20, y=50)

##backbtn
#lblb = Button(readRFID, highlightbackground='black', command=lambda: mainMenu.show_frame(mainMenu),font=("Helvetica", 16), width=7, text='← Back') # <- <- <- backbtn
#lblb.place(x=20, y=40)
#others

##READ RFID:
lblrr=Button(mainMenu, text="🂡 Read RFID",  fg='blue', bg= 'red',highlightbackground='black', command=lambda: readRFID.tkraise() ,font=("Helvetica", 16), width=27)
lblrr.place(x=20, y=50)

def scanForRFID():
        print("Placeholder")
        ##Enter rfid scanning code here

lfrfid = Button(readRFID, text="Listen for RFID/NFC frequency", command=lambda: scanForRFID(), font=("Helvetica", 16), width=27)
lfrfid.place(x=20, y=200)

##Write RFID
lblrw=Button(mainMenu, text="✎ Write RFID" ,fg='#72C272',bg= 'black', highlightbackground='black',  font=("Helvetica", 16), width=27)
lblrw.place(x=20, y=100)
lblwa=Button(mainMenu, text="ᯤ Wifi Attacks", fg='red',bg= 'red',highlightbackground='black',  font=("Helvetica", 16), width=27)
lblwa.place(x=20, y=150)

root.title('Basilisk V1')
root.resizable(False, False)
root.geometry("320x480")
root.configure(bg='black')
root.mainloop()