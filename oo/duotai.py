from cat import Cat
from mouse import Mouse
from  person import Person

tom=Cat("tom")
jerry=Mouse("jerry")

tom.eat()
jerry.eat()

p1=Person("soderberg",18)
p1.feedAnimal(tom)
p1.feedAnimal(jerry)
