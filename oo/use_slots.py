
class Person(object):
    __slots__ = ("name", "age", "speak")  # limit add property and method dynamically(only given turple value)


p1 = Person()
# p1.height = 100
# print(p1.height)
p1.name="aaa"
print(p1.name)