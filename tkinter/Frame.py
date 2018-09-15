import tkinter
# from tkinter import ttk

win = tkinter.Tk()
win.title("menu using")
win.geometry("400x400+200+200")

#container control
frm=tkinter.Frame(win)
frm.pack()
#left
frm_1=tkinter.Frame(frm)
tkinter.Label(frm_1,text="left top",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1,text="left bottom",bg="blue").pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)


#right
frm_2=tkinter.Frame(frm)
tkinter.Label(frm_2,text="right top",bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_2,text="rigt bottom",bg="white").pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)

win.mainloop()
