import tkinter
win = tkinter.Tk()

win.title("Soderberg")
win.geometry("400x400+200+200")
listbox2=tkinter.Listbox(win,selectmode=tkinter.EXTENDED) #SUPPORT cotrl key or shift select
listbox2.pack()
for item in ["good", "nice", "handsome","good", "nice", "handsome","good", "nice", "handsome","good", "nice", "handsome"]:
    listbox2.insert(tkinter.END, item)


win.mainloop()