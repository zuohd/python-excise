f = open("hello.txt", "r")
c = f.readlines()
print(type(c))
f.close()
for l in c:
    print(l)
