import time
import threading

def longIO(callback):
    def run(cb):
        print("start long time operation")
        time.sleep(5)
        print("Ending long time operation")
        cb("Hello I'm returned ")
    threading.Thread(target=run,args=(callback,)).start()

def finish(data):
    print("start handle calling function")
    print("receieve the longIO Data:",data)
    print("Ending handle calling function")

def reqA():
    print("start handle request A")
    longIO(finish)
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
