class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other

    def __radd__(self, other):
        print('radd',self.data,other)
        return other+self.data

    def __repr__(self):
        return "add repr {0}".format(self.data)

    def __str__(self):
        return 'N:{0}'.format(self.data)

x=Adder(3)
print(1+x)
print(x)
print((str(x),repr(x)))

