import  threading

def run():
    print("hello")

if __name__ == '__main__':
    t=threading.Timer(5,run) #delay 5 seconds

    t.start()
    t.join()

    print("Main thread endding..")