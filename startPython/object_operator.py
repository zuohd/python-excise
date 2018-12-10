class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __getitem__(self, item):
        return item ** 2

    def __getattr__(self, item):
        if item == "age":
            return 35
        else:
            raise AttributeError


a = Number(4)
b = a - 2
print(type(b))
print(b.data)

for i in range(5):
    I = a
    print(I[i])
print(a.age)