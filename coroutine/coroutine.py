# present stack execute order
# def A():
#     print("A Start")
#     B()
#     print("A end")
# def B():
#     print("B Start")
#     C()
#     print("B end")
#
#
# def C():
#     print("C Start")
#     print("C end")
#
# A()
#yield get function to execute in different stages
def fun():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

r=fun()
print(next(r))
print(next(r))
print(next(r))
