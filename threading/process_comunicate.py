import os,time
from multiprocessing import  Process,Queue

def write(q):
    print("write process start...%s"%(os.getpid()))

    for chr in ["A","B","C","D"]:
        q.put(chr)
        time.sleep(1)
    print("write process end...%s"%(os.getpid()))

def read(q):
    print("Read process start...%s"%(os.getpid()))
    while True:
        value=q.get()
        print("value is "+value)
    print("Read process start...%s"%(os.getpid()))


if __name__ == '__main__':
    # Parent process create quenue and pass it to child process
    q=Queue()
    cp1=Process(target=write,args=(q,))
    cp2=Process(target=read,args=(q,))

    cp1.start()
    cp2.start()

    cp1.join()
    cp2.terminate()

    print("Main process end")
