import functools

print(int("10",base=10))

print(int("1010",base=2))

# pian function
def int2(str,base=2):
    return int(str,base)

#fixed some parameter and pass function name
int3=functools.partial(int,base=2)

print(int3("1011"))