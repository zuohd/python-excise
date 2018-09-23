import time

def longIO():
    print("start long time operation")
    time.sleep(5)
    print("Ending long time operation")

def reqA():
    print("start handle request A")
    longIO()
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
