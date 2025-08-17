import customtkinter as tk
from tkinter import filedialog

def startMainScreen():
    main_window = tk.Tk()
    main_window.button
    main_window.title("My Application")
    main_window.geometry("800x600")
    main_window.mainloop()


def getFileDirectory():
    directory = filedialog.askdirectory()