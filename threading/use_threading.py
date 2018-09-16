# threading share one process memory space
# it's minimum execute unit,multiple threading share one variant

# import  _thread,threading--first module is low level,seconde is the first's wrap module

import threading
import time

a=100
def run(num):
    print("Child threading start--%s" % (threading.currentThread().name))
    time.sleep(3)
    global a
    a+=1
    print("doing something",a)
    time.sleep(3)
    print("Child threading end--%s" % (threading.currentThread().name))


if __name__ == '__main__':
    print("Main threading start--%s" % (threading.currentThread().name))
    a += 2
    t = threading.Thread(target=run, name="fooThread",args=(2,))
    t.start()
    # a+=1
    t.join()  # join method:main thread will be waiting for child thread ending

    print("a=%d"%a)
    print("Main threading end--%s" % (threading.currentThread().name))
