import threading
import time

sem = threading.Semaphore(3)


def run():
    with sem:
        for i in range(5):
            print("%s-%d" % (threading.currentThread().name,i))
            time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()
