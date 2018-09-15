import tkinter

win=tkinter.Tk()
win.title("sample")
win.geometry("400x400+200+20")

def func(event):
    print(event.x,event.y)

button1=tkinter.Label(win,text="mouse left click")
'''
<Button-1> :left button
<Button-2>:scroll wheel
<Button-3>:right button
<Double-Button-1>:double click left,change number as the same as click
<Triple-Button-1>:three click,change number as the same as click
<key>:keyboard event,need to set focus
<Return>:Enter
<BackSpace>:back 
<Shift_L>:left shift key
keyname:press specific key 
<Control-Alt-a>:group keys event
<Shift-Up>:shift+up arrow event
'''
button1.bind("<Button-1>",func) #left button of mouse

# press mouse and move event
button1.bind("<B1-Motion>",func)

button1.pack()
win.mainloop()