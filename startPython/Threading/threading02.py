import threading
import time
class Mythreading(threading.Thread):
    def __init__(self,conn):
        super(Mythreading,self).__init__()
        self.conn=conn
    def run(self):
        print("run task",self.conn)
        time.sleep(5)
t1=Mythreading("t1")
t2=Mythreading("t2")
t1.start()
t2.start()