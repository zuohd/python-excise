try:
    print(3 / 0)
except NameError as e:
    print("no num")
except ZeroDivisionError as e:
    print("error" + str(e.args))
else:
    print("right")

try:
    print(num)
except (NameError, ZeroDivisionError):
    print("some erros")

try:
    print(int("abc"))
except BaseException as e:  # BaseException is base class of all exceptions
    print(str(e.args))

try:
    print(2 / 1)
except:
    print("e")
finally:
    print("always running")
