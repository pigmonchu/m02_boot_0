from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    size = "1024x768"
    
    def __init__(self):
        Tk.__init__(self)
        
        self.geometry(self.size)
        self.title("Mi ventana")
        self.configure(bg = "blue")

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = mainApp()
    
    app.start()

