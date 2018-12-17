def f1():
    name="soderberg"
    def f2():
        # name="eric"
        print(name)
    return f2()

f1()

li=[lambda x:x for x in range(10)]
print(li)