from multiprocessing import  Pool
import os, time, random


def run(name):
    print("Child process %s start--%s" % (name, os.getpid()))
    start=time.time()
    time.sleep(random.choice([1,2,3]))
    end=time.time()
    print("Child process %s end--%s,executed time %.2f" % (name, os.getpid(),end-start))


if __name__ == '__main__':
    print("main process start")

    pp = Pool(2)  # use process pool,default size is cpu number

    for i in range(4):
        pp.apply_async(run, args=(i,))

    pp.close()  # close method need to before join method,and after close we can't add new process
    pp.join()  #main process will wait for all child processes in process pool

    print("main process end")
