class SpecialMembers:
    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)
obj=SpecialMembers()
obj["2"]

obj["k1"]="aaa"

del obj['k1']
