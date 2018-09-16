from multiprocessing import Process
from time import sleep

num = 100


def childRun1():
    print("child process 1 start..")
    global num #different variant which is just backup of num
    num += 1
    print(num)
    print("child process 1 end..")

def childRun2():
    print("child process 2 start..")
    global num
    num += 1
    print(num)
    print("child process 2 end..")

if __name__ == '__main__':
    print("Main process start....")
    cp1 = Process(target=childRun1)
    cp1.start()

    cp2 = Process(target=childRun2)
    cp2.start()

    cp1.join()
    cp2.join()

    print("Main process end.num:%d" % num)  # child process variant don't impact parent process variant.
