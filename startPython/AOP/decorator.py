def decorator(func):
    def inner(*args, **kwargs):
        print("--before function execute--")
        func(*args, **kwargs)
        print("--After executed function--")

    return inner

@decorator
def func(arg):
    print(arg)


func("hello")
