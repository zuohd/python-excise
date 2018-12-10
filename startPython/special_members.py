class SpecialMembers:
    def __init__(self):
        self.name="soderberg"
        self.blog="https//zuohd.github.io"

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)
    def __iter__(self):
        yield 1
        yield 2
        yield 3

obj=SpecialMembers()
print(SpecialMembers.__dict__)
print(obj.__dict__)
obj["2"]

obj["k1"]="aaa"

del obj['k1']

for i in obj:
    print(i)
