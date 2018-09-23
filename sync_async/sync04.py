import time
import threading


def longIO():
    print("start long time operation")
    time.sleep(5)
    print("Ending long time operation")
    yield "Hello,I'm returned"


def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen1 = func()  # reqA
        gen2 = next(gen1)  # longIO

        def run(g):
            res = next(g)
            try:
                gen1.send(res)  # return reqA data
            except StopIteration as e:
                pass

        threading.Thread(target=run, args=(gen2,)).start()

    return wrapper


@genCoroutine
def reqA():
    print("start handle request A")
    res = yield longIO()
    print("receieve the longIO Data:" + res)
    print("Ending handle request A")


def reqB():
    print("start handle request B")
    time.sleep(2)
    print("Ending handle request B")


def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == '__main__':
    main()
