'''
use multiple condition
and elif
'''
age = 12
if age >= 0 and age <= 120:
    print("valid")
else:
    print("invalid")

python_score = 50
c_score = 70

if python_score > 60:
    print("python is passed")
    if c_score > 60:
        print("python and c are passed")
    else:
        print("C is not passed")
else:
    print("Pythone is not passed")

is_employee = True

if not is_employee:
    print("He is not an employee")
else:
    print("He is  allowed")
