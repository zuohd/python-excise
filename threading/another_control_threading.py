import threading
import time

bar = threading.Barrier(2)


def run():

    print("%s-start" % (threading.currentThread().name))
    time.sleep(1)
    bar.wait()

    print("%s-end" % (threading.currentThread().name))


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()
