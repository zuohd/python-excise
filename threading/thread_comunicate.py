import threading
import time


def run():
    event = threading.Event()

    def fun():
        for i in range(5):
            event.wait()
            event.clear()
            print("Hello%d" % i)

    t = threading.Thread(target=fun).start()
    return event


e = run()

for n in range(5):
    time.sleep(2)
    e.set()