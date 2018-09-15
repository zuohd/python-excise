import tkinter

win=tkinter.Tk()
win.title("sample")
win.geometry("400x400+200+20")

label1=tkinter.Label(win,text="good",bg="blue")
label2=tkinter.Label(win,text="Nice",bg="red")
label3=tkinter.Label(win,text="great",bg="pink")
# label1.place(x=10,y=10)
# label2.place(x=20,y=20)
# label3.place(x=50,y=50)  --absolute layout

# label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
# label2.pack(fill=tkinter.X,side=tkinter.LEFT)
# label3.pack() # realtive layout

'''
grid layout
'''
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
win.mainloop()