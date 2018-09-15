import soderberg

# import specific part to current namespace[or * means all functions and variables]
from company import say_nice, say_good
import functions.hello as hello

# def say_nice():
#     print("hello world")


soderberg.say_good()
soderberg.say_handsome()
soderberg.say_nice()
say_nice()
say_good()
hello.say_nice()
print(soderberg.TT)
