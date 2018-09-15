#simple closure



def outer(func):
    def innner(age):
        if age<0:
            age=0
        func(age)
    return innner;

@outer
def func1(age):
    # print("*********")
    print("soderberg is a good man,I'm %d years old." % age)

# f=outer(func1)
func1(-10)