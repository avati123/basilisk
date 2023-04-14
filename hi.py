import tkinter as tk
from PIL import Image, ImageTk


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Title")
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.frames = {}

        for F in (StartPage, Page1):
            frame = F(self.container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.update()
        self.show_frame(StartPage)

    def show_frame(self, cont):  # cont = page_name
        if cont not in self.frames:
            self.frames[cont] = cont(self.container, self)
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='StartPage').pack()
        self.bind("<<ShowFrame>>", self.myStartPage)
        self.controller = controller

    def printcehck(self, event):
        print("hack")

    def myStartPage(self, controller):
        super(StartPage).__init__()
        print(controller)
        self.controller.show_frame(Page1)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='Page1').pack()


if __name__ == '__main__':
    tkinterApp().mainloop()