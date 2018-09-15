print(1 + 2)
print("1" + "2")


class Person(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):  # other is the second object
        return Person(self.num + other.num)

    def __str__(self):
        return str(self.num)


per1 = Person(2)
per2 = Person(3)
print(per1 + per2)
print(per1.__add__(per2))
