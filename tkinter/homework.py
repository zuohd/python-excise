import  tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self,master,path):
        frame=tkinter.Frame(master)
        frame.pack()
        self.tree=ttk.Treeview(frame)
        self.tree.pack()
        root=self.tree.insert("","end",text=os.getcwd().split("/")[-1],open=True)
win=tkinter.Tk()
win.title("homework")
win.geometry("600x400+20+20")
treewin=TreeWindows(win,"/home")
win.mainloop()