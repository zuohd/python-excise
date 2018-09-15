'''
Define function && calling function
'''


def hello(name):
    return "Hi " + name


def add(a, b, c=0):  # c is default parameter,should the last one
    return a + b + c


def empty():
    print("youyou")
    # return None


def substract(a, b):
    return a - b


empty()
print(add(3, 4))
print(add(1, 2, 3))
print(hello("Soderberg"))
print(substract(b=3, a=4))  # keyword parameter


def func(*arr):  # uncetain length parameters
    for x in arr:
        print(x)


func("china", "xxx", "yyyy", "abc")


def my_sum(*n):
    sum = 0
    for i in n:
        sum += i
    return sum


print(my_sum(1, 2, 3, 4))


def func2(**kwargs):  # uncertain length keyword parameter
    print(kwargs)


func2(a=3)


# the below can passing any parameters
def func3(*args, **kwargs):
    pass


# anonymous function=lambda function,there is not need to 'def' keyword
'''
lambda body is an expression instead of code block
formate:lambda arg1,arg2,grg3,....,argn:expression
'''

l1 = lambda a, b: a + b
print(l1(5, 6))

