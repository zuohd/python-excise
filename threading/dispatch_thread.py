import threading
import time

condition = threading.Condition()  # threading condition variant


def run1():
    with condition:
        for i in range(0, 10, 2):
            print(threading.currentThread().name, i)
            time.sleep(3)
            condition.wait()
            condition.notify()


def run2():
    with condition:
        for i in range(1, 10, 2):
            print(threading.currentThread().name, i)
            time.sleep(1)
            condition.notify()
            condition.wait()


threading.Thread(target=run1).start()
threading.Thread(target=run2).start()
