class Person(object):
    name="Jack" #class property,calling by className.name
    def __init__(self,name):
        self.name=name # object property-priority is higher than class property,calling by object.name

Person.a=1
print(Person.a)
print(Person.name)
p1=Person("Soderberg")
print(p1.name)

p2=Person("lilei")
print(Person.a)
print(p2.name)
del p2.name #after delete object property,the value will be the same named class property value
print(p2.name)