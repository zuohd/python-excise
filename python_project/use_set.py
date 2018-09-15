'''
set like dictionary,one group of keys,there are not values.

It's unordered and unduplicated element
'''

#creat set
s1=set([1,2,3,4,5,4,5])

print(s1)
print(type(s1))

s2=set((1,2,3,3,2,1))
print(s2)

s3=set({"tom":20,"soderberg":50})
print(s3)

s1.add(6)
print(s1)

s4={1,2,3,4,5}
s4.update([6,7,8])
s4.update((9,11))
s4.update("soderberg")
s4.remove(3)
print(s4)
print(type(s4))

for i in s4:
    print(i)

for index,data in enumerate(s4):
    print(index,data)



s5=set([4,5,6])
s6=set([4,7,9])
a1=s5 & s6
a2=s5 | s6

print(s5.intersection(s6))
# print(a1)
# print(a2)
print(s5.union(s6))
print(s5.difference(s6))
s7=list(s5)
# print(s7.extend())