str1 = "soderberg is a good mand!"
str2 = 'soderberg is a nice man!'
str3 = "soderberg is a handsome man!"

# string calculate
# concat string
str4 = "soderberg is"
str5 = " a good man!"
# print(str4)
# print(str5)
print(str4 + str5)
print(str4 * 3)
# str4[1]="e"
print(str4[1])  # zero indexed

str6 = "soderberg is a good man!"
str7 = str6[10:19]
str9 = str6[:19]
str8 = str6[10:]
print(str7)
print(str8)
print(str9)

print("be" in str6)
print("be" not in str6)
print(str6.index("be"))

print("str6 is %s" % str6)

# zhuanyi character
# \n

print("soderber is \\n good man")

print("soderberg is a \"good\" man")  # \" ,\'

# The following is multiple lines output
print('''
good
nice
man
''')

print("soderberg\tgood\tman")  # \t means table character

print("\\\t\\")
print(r"\\\t\\")

print("3+4")
print(eval("3+4"))

print(eval("3<4"))
print(type(eval("3<4")))

print(len(str6))

print(("SODerBERG").lower())
print(str6.upper())

str10 = "soderberg Is A MaN!"
print(str10.swapcase())
print(str10.capitalize())
print(str10.title())
# print("wordiswrong".title())
print(str10.center(30,"1"))

print(str10.ljust(30,"*"),"%")
print(str10.rjust(30),"%")

print(str10.zfill(40))
print(str10.count("de"))
print(str10.find("ac",0))

print(str10.rfind("er"))
print(str10.index("er"))
print(str10.rindex("er"))

print("*****xxxx".lstrip("*"))
print("xxxx***".rstrip("*"))
print("***xxxx***".strip("*"))

print(ord("a"))
print(chr(97))
print(ord("\n"))