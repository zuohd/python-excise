class Person(object):

    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money  # __money can't access outside but _Person__money can be access

    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

    def eat(self):
        print("%s is eating" % self.name)

    def run(self, speed):
        # print(self.__money)
        print("running at %d" % (speed))

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)

    def __del__(self):
        print("this is destructor function")


p1 = Person("soderberg", 30, 180, 80, 10000000)
# p1.__money=0
# print(p1.__money)
p1.setMoney(0)
print(p1.getMoney())
p1.a = 30 #add property dynamic
print(p1.a)
p1.run(15)
print(p1._Person__money)