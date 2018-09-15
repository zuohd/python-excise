import tkinter

win = tkinter.Tk()
win.title("hello")
win.geometry("400x400+200+20")

sc1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=100,
                    length=200)  # VERTICAL is another orientation
sc1.pack()

button = tkinter.Button(win, text="click", command=lambda: print(sc1.get()), width=20, height=5)
button.pack()

v = tkinter.StringVar()
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1,
                     textvariable=v, command=lambda: print(v.get()))  # values=(0,2,4,6,8)

sp.pack()
v.set(20)
win.mainloop()
