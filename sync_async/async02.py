import time
import threading
gen=None
def longIO():
    def run():
        print("start long time operation")
        time.sleep(5)
        try:
            global gen
            gen.send("Hello I'm returned ")
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()



def reqA():
    print("start handle request A")
    res=yield longIO()
    print("receieve the longIO Data:"+res)
    print("Ending handle request A")


def reqB():
    print("start handle request B")
    time.sleep(2)
    print("Ending handle request B")


def main():
    global gen
    gen=reqA()
    next(gen)
    reqB()
    while 1:
        time.sleep(0.1)
        pass


if __name__ == '__main__':
    main()
