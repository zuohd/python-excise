import tkinter
from tkinter import ttk

win=tkinter.Tk()
win.title("sample")
win.geometry("400x400+200+20")


tree=ttk.Treeview(win)
tree["columns"]=("name","sex","height","weight")

tree.column("name",width=100)
tree.column("sex",width=50)
tree.column("height",width=50)
tree.column("weight",width=50)

tree.heading("name",text="name")
tree.heading("sex",text="sex")
tree.heading("height",text="height")
tree.heading("weight",text="weight")


tree.insert("",0,text="line1",values=("Jack","boy","165","80"))
tree.insert("",1,text="line2",values=("Rose","girl","165","80"))

tree.pack()
win.mainloop()