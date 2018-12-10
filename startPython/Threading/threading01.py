import threading
import time
def print_time(string):
    print("task",string)
    time.sleep(5)


t1=threading.Thread(target=print_time,args=('t1',))
t1.start()
t2=threading.Thread(target=print_time,args=('t2',))
t2.start()
t3=threading.Thread(target=print_time,args=('t3',))
t3.start()