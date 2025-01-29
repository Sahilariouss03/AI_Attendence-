from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x720+0+0")
        self.root.title("Register A Student")
        
    if __name__ == "__main__":
        root = Tk()
        obj = Student(root)
        root.mainloop()