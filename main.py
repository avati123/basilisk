import tkinter as tk
from tkinter import *
from tkinter import font

window=Tk()

style = font.Font(size=25)
style2 = font.Font(size=30)
readRFID = Frame(window)
writeRFID = Frame(window)
wifiattacks  = Frame(window)
background  = Frame(window)

readRFID.grid(row=0, column=0)
writeRFID.grid(row=0, column=0)
wifiattacks.grid(row=0, column=0)
background.grid(row=0, column=0)

readRFIDlabel = Label(readRFID, text='Page 1', font=style)
writeRFIDlabel = Label(writeRFID, text='Page 2', font=style)
wifiattackslabel = Label(wifiattacks, text='Page 3', font=style)
backgroundlabel = Label(background, font=style, text=' ')
readRFIDlabel.pack(pady=230, padx=120)
writeRFIDlabel.pack(pady=230, padx=120)
wifiattackslabel.pack(pady=230, padx=120)
backgroundlabel.pack(pady=230, padx=120)



# buttons
lblrr=Button(window, text="🂡 Read RFID",  fg='blue', bg= 'red',highlightbackground='black', command=lambda: readRFID.tkraise() ,font=("Helvetica", 16), width=27)
lblrr.place(x=20, y=50)
##backbtn
lblb = Button(readRFID, highlightbackground='black', command=lambda: window.tkraise() ,font=("Helvetica", 16), width=7, text='← Back')
lblb.place(x=20, y=40)
#others
lblrw=Button(window, text="✎ Write RFID" ,fg='#72C272',bg= 'black', highlightbackground='black',  font=("Helvetica", 16), width=27)
lblrw.place(x=20, y=100)
lblwa=Button(window, text="ᯤ Wifi Attacks", fg='red',bg= 'red',highlightbackground='black',  font=("Helvetica", 16), width=27)
lblwa.place(x=20, y=150)



window.title('Basilisk V1')
window.resizable(False, False)
window.geometry("320x480")
window.configure(bg='black')
window.mainloop()