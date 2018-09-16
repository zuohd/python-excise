'''
A task is a process for os

 include:data segment/code block/stack heap segments

'''

# run()

from multiprocessing import Process  # cross platform
import os  # os.fork just support linux/unix platform
from time import sleep


def run1(paramter):
    while True:
        print("soderberg is %s--pid:%s,ppid:%s" % (paramter, os.getpid(), os.getppid()))
        sleep(1.5)


def run2():
    print("cp start")
    sleep(3)
    print("cp end")


if __name__ == '__main__':
    print("Main(parent) process--pid:%s" % (os.getpid()))
    # create child process
    # cp = Process(target=run, args=("great",))
    cp = Process(target=run2)

    # start
    cp.start()
    # cp.join()  #parent process will wait for child process
    print("main end")  # if not calling join method, child process don't care parent process ending

    # while True:
    #     print("soderberg is good")
    #     sleep(1)
