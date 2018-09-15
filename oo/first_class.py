'''
Class design:
class name/properties/method

name it Camel principle
class is not occupy the memory space,it's a type


'''


class Wife(object):  # object is base class(super class)
    # name = ""
    # age = 0
    # height = 0
    # weight = 0
    def __init__(self, name, age, height, weight):  # constructor
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):  # method first parameter must be self
        print("%s is eating" % self.name)

    def run(self, speed):
        print(self)
        print("running at %d" % (speed))

    def __str__(self): # means tostring(__repr__,buildin calling)
        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)

    def __del__(self):  # destructor function:free object
        print("this is destructor function")
