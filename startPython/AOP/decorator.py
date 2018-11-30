def decorator(func):
    def inner(*args, **kwargs):
        print("--before function execute--")
        ret = func(*args, **kwargs)
        print("--After executed function--")
        return ret

    return inner

@decorator
def func(arg):
    print(arg)


func("hello")
