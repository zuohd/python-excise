from types import MethodType
'''
Create empty class
'''


class Person(object):
    pass


per = Person()

# Add property dynamically
per.name = "zuohd"
print(per.name)

def say(self):
    print("hello")

#Add method dynamic
per.speak=MethodType(say,per)
per.speak()

# Person.speak=MethodType(say,Person)
# per.speak()