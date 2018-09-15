from collections import Iterable,Iterator
s1=set([1,2,3])
l1=[1,2,3]

print(isinstance(s1,Iterable))
print(isinstance(l1,Iterable))

print(isinstance(s1,Iterator))
print(isinstance(l1,Iterator))
print(isinstance((x for x in range(10)),Iterator))



l=(x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))



#covert list to Iterator,call iter
a=iter([1,4,5])
print(next(a))
print(next(a))
print(next(a))
