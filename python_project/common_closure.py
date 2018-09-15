def outer(func):
    def inner(*args,**kwargs):
        # add handle code block
        print("*******") #example code
        func(*args,**kwargs)
    return inner

@outer
def say(name,age):
    print("%s,%s" %(name,age))

say("soderberg",18)