import threading
import time


def print_time(string):
    print("task ", string)
    time.sleep(1)


for i in range(50):
    t = threading.Thread(target=print_time, args=('t={0}'.format(i),))
    t.start()
    t.join()
