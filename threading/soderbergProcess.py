import os
import time
from multiprocessing import Process


# wrap specific feature process to class
class SoderbergProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name=name

    def run(self):
        print("Child process %s start,pid is %s"%(self.name,os.getpid()))

        time.sleep(3)
        print("Child process %s end,pid is %s"%(self.name,os.getpid()))
