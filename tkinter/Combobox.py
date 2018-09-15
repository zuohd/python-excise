import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("menu using")
win.geometry("400x400+200+200")
cv = tkinter.StringVar()

combox = ttk.Combobox(win, textvariable=cv)
combox.pack()
combox["value"] = ("China", "United states", "Russian")
combox.current(0)


def func(event):
    print(combox.get())
    print(cv.get())


combox.bind("<<ComboboxSelected>>", func)
win.mainloop()
