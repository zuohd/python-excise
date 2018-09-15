class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("eating")
    def run(self):
        print("run")
    def feedAnimal(self,animal):
        print("....food")
        animal.eat()