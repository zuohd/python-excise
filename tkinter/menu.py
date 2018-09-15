import tkinter

def func():
    pass
win=tkinter.Tk()
win.title("menu using")
win.geometry("400x400+200+200")

menubar=tkinter.Menu(win)
win.config(menu=menubar)

menu1=tkinter.Menu(menubar,tearoff=False)
for item in ["File","View","Exit"]:
    if item=="Exit":
        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=func)

menubar.add_cascade(label="language",menu=menu1)
# menubar.pack()
win.mainloop()