import copy
a=2
b=a
c=copy.copy(a)
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
a=3
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))