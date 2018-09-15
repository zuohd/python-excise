import tkinter


def func():
    print("power")


def updateData():
    if hobby1.get():
        print("money")
    if hobby2.get():
        print("people")
    if hobby3.get():
        print("love")
    if hobby4.get():
        print("power")


def printRadioValue():
    print(r.get())


win = tkinter.Tk()

win.title("Soderberg")
# win.geometry("400x400+200+200")
button = tkinter.Button(win, text="Print", command=func, width=10, height=2)
button.pack()

button1 = tkinter.Button(win, text="Exit", command=win.quit, width=10, height=2)
button1.pack()

button2 = tkinter.Button(win, text="lambda use", command=lambda: print("ehllo"), width=10, height=2)
button2.pack()

entry = tkinter.Entry(win, show="*")  # password showing
entry.pack()

e = tkinter.Variable()
entry1 = tkinter.Entry(win, textvariable=e)
entry1.pack()

e.set("xxxx")
print(e.get())  # the same function use entry.get(),too

button3 = tkinter.Button(win, text="output entry value", command=lambda: print(entry1.get()), width=10, height=2)
button3.pack()

scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=4)  # textarea control
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''
　If there is anyone out there who still doubts thatAmerica is a place where all things are possible; whostill wonders if the dream of our founders is alive inour time; who still questions the power of ourdemocracy, tonight is your answer.

该文章《奥巴马竞选的演讲稿》来源于出国留学网，网址：https://www.liuxue86.com/a/3395085.html
'''

text.insert(tkinter.INSERT, str)
hobby1, hobby2, hobby3, hobby4 = tkinter.BooleanVar(), tkinter.BooleanVar(), tkinter.BooleanVar(), tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updateData)
check2 = tkinter.Checkbutton(win, text="people", variable=hobby2, command=updateData)
check3 = tkinter.Checkbutton(win, text="love", variable=hobby3, command=updateData)
check4 = tkinter.Checkbutton(win, text="power", variable=hobby4, command=updateData)
check1.pack()
check2.pack()
check3.pack()
check4.pack()

r = tkinter.IntVar()
radio = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=printRadioValue)
radio.pack()
radio1 = tkinter.Radiobutton(win, text="one", value=2, variable=r, command=printRadioValue)
radio1.pack()

listbox = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
listbox.pack()
for item in ["good", "nice", "handsome"]:
    listbox.insert(tkinter.END, item)

listbox.insert(tkinter.ACTIVE, "cool")
listbox.insert(tkinter.END, ["very good", "very nice"])
print("listbox has %d" % listbox.size())
# listbox.delete(1, 3)  # startindex,endindex
listbox.select_set(1)  # select element
# listbox.select_clear(1)
print(listbox.get(2, 4))
print(listbox.curselection())  # selected item index
print(listbox.select_includes(1)) #if selected on one element

lbv=tkinter.StringVar()
listbox1=tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
listbox1.pack()
for item in ["good", "nice", "handsome"]:
    listbox1.insert(tkinter.END, item)
print(lbv.get())
# lbv.set(("1","2","3"))

def myPrint(e):
    print(listbox1.curselection())
listbox1.bind("<Double-Button-1>",myPrint)

listbox2=tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
listbox2.pack()
for item in ["good", "nice", "handsome"]:
    listbox2.insert(tkinter.END, item)

win.mainloop()
