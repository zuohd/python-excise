import threading
def runthreading(event):
    print("start...")
    event.wait()
    print("End...")

event_obj=threading.Event()
for n in range(10):
    t=threading.Thread(target=runthreading,args=(event_obj,))
    t.start()
event_obj.clear()
inp=input("give me a bool value:")
if inp=="True":
    event_obj.set()