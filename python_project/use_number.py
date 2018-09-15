import math
import random
"""
Python can handle any types:int,float,complex
format is like maths
"""

num1 = 10
# print(id(num1))
num2 = num1
# print(id(num2))
num3 = num4 = num5 = 1
# print(id(num3))
# print(id(num4))
# print(id(num5))
print(num3, num4, num5)
num6, num7 = 6, 7
print(num6, num7)

# float include int and point parts

f1 = 1.1
f2 = 2.2
print(f1 + f2)

# complex form as a+bj

'''
number type convertor
'''
print(int(f1))
print(float(1))
print(int("123"))
print(float("23.4"))
print(int("+123"))
print(int("-123"))

# math function

a = -10
print(abs(a))
print(6 > 9)
print(max(3, 4, 232, 4))
print(min(3, 4))
print(pow(2, 3))  # calculat 2^3
print(round(3.546,2))
print(round(3.546,1))


print(math.ceil(18.1))
print(math.ceil(18.9))
print(math.floor(18.1))
print(math.floor(18.9))
print(math.sqrt(16))
print(math.modf(22.3)) #return int and decimal parts


# random generator
print(random.randint(1,3))
print(random.choice([2,4,55,1,3])) #fetch from sequence randomly
print(random.choice([2,"aaa"]))
print(random.choice(range(5))) #range(5)=[0,1,2,3,4]
print(random.choice("soderberg"))
print(random.choice(range(100))+1)
print(random.randrange(1,100,2)) # parameter formate ([start,]stop[,step])

list=[1,2,3,4,5]
random.shuffle(list)
print(list)
print(random.uniform(3,9)) #real decimal random

print(5/3)
print(5//3)
print(5**3)
a=3
b=2
# a%=b
a//=b
print(a)
