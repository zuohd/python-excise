import tkinter


def showMenu(event):
    menubar.post(event.x_root, event.y_root)


win = tkinter.Tk()
win.title("menu using")
win.geometry("400x400+200+200")

menubar = tkinter.Menu(win)

menu = tkinter.Menu(menubar, tearoff=False)
for item in ["File", "View", "Exit"]:
    menu.add_command(label=item)

menubar.add_cascade(label="language", menu=menu)
win.bind("<Button-3>", showMenu)
win.mainloop()
