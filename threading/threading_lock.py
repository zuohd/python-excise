import threading
import time

a = 0

lock = threading.Lock()



# multiple thread cause data exception
def run(num):
    # print("Child threading start--%s" % (threading.currentThread().name))
    global a
    for i in range(10000000):
        # add thread lock,the lock code block will be running in single threading mode
        lock.acquire()
        try:
            a = a + num
            a = a - num
        finally:
            lock.release()  # release lock

        '''
        Use 'with' grammar to add lock and release lock dynamically,
        to avoid dead lock.
        
        with lock:
            a += num
            a -= num
        '''
    # print("Child threading end--%s" % (threading.currentThread().name))


if __name__ == '__main__':
    print("Main threading start--%s" % (threading.currentThread().name))

    t1 = threading.Thread(target=run, name="foo1", args=(2,))
    t2 = threading.Thread(target=run, name="foo2", args=(9,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("a=", a)
    print("Main threading end--%s" % (threading.currentThread().name))
