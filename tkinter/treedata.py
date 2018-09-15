import tkinter
from tkinter import ttk

win=tkinter.Tk()
win.title("sample")
win.geometry("400x400+200+20")

tree=ttk.Treeview(win)
tree.pack()


#one level
treeFirst1=tree.insert("",0,"zh-cn",text="China",values=("Hebei",""))
treeFirst2=tree.insert("",1,"usa",text="America",values=("Hebei","Shanxi"))
treeFirst3=tree.insert("",2,"en",text="England",values=("Hebei","Shanxi"))

#second level
treeFirst1_1=tree.insert(treeFirst1,0,"HB",text="He Bei",values=("hb"))
treeFirst1_2=tree.insert(treeFirst1,1,"SX",text="Shanxi",values=("sx"))
treeFirst1_3=tree.insert(treeFirst1,2,"HLJ",text="Heilongjiang",values=("hlj"))

treeFirst2_1=tree.insert(treeFirst2,0,"dex",text="He Bei",values=("hb"))
treeFirst2_2=tree.insert(treeFirst2,1,"newyork",text="Shanxi",values=("sx"))
treeFirst2_3=tree.insert(treeFirst2,2,"ditelv",text="Heilongjiang",values=("hlj"))

treeFirst1_1_1=tree.insert(treeFirst1_1,0,"CZ",text="Cang Zhou")
treeFirst1_1_2=tree.insert(treeFirst1_1,0,"SJZ",text="Shi jia zhuang")
treeFirst1_1_3=tree.insert(treeFirst1_1,0,"XT",text="Xing Tai")

win.mainloop()