import common

def run():
    inp=input("input calling function name:")
    func=getattr(common,inp)
    func()

run()