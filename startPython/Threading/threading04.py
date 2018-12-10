import threading
class MyThreading(threading.Thread):
    def __init__(self):
        super(MyThreading,self).__init__()
    def run(self):
        print("I'm subthreading.",threading.current_thread())
t=MyThreading()
t.start()
print("Main thread:",threading.current_thread())
print("threading count:",threading.active_count())