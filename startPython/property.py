class User:
    @property
    def firstName(self):
        print("class property")

    @firstName.setter
    def firstName(self, value):
        print("first name is {0}".format(value))

    @firstName.deleter
    def firstName(self):
        print("firstname is deleted")

    def f1(self):
        print("f1")

    def f2(self,value):
        print("f2")

    def f3(self):
        print("f3")

    specialfields = property(fget=f1, fset=f2, fdel=f3, doc="I'm comment")


soderberg = User()
soderberg.firstName = 33
soderberg.firstName
del soderberg.firstName

soderberg.specialfields
soderberg.specialfields="abc"
del soderberg.specialfields

print(User.specialfields.__doc__)
