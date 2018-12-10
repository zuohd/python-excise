class AccessControl:
    def __setattr__(self, key, value):
        if key == "name":
            self.__dict__[key] = value
        else:
            raise AttributeError(key + ' not allowd.')
a=AccessControl()
a.name="selfnumber"
print(a.name)
a.age=30