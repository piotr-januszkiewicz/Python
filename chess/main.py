import tkinter as tk
from PngImport import PngImport as png
from tkinter import ttk

image = png()

class Window:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("chess")
        self.window.geometry("1002x602")

        self.window.iconbitmap(image.icon)
        menu = Menu(self.window)
        menu.display_menu()
        self.window.resizable(False, False)
    def display_window(self):
        self.window.mainloop()

class Menu(Window):
    def __init__(self, window):
        self.photo = tk.PhotoImage(file=image.main_menu)
        self.image_label = ttk.Label(
            window,
            anchor=tk.E,
            image=self.photo,
            padding=-1
        )
    def display_menu(self):
        self.image_label.pack()



game = Window()

game.display_window()



