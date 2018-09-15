import re

'''
string split
'''

str1="Tom is a good good good   cat"

print(str1.split(' '))
print(re.split(r" +",str1))

print(re.sub(r"(good)","nice",str1))
print(re.subn(r"(good)","nice",str1))

#reg group:
# use () is a group
str2="010-23457845"
m=re.match(r"(?P<first>\d{3})-(?P<last>\d{8})",str2)
print(m.group(0)) #group(0) is original string
print(m.group(1))
print(m.group(2))
print(m.groups())

print(m.group("first"))


'''compile:when use reg expression,re will do the two things:
1.if reg expression is not valid,will raise error
2.use compiled regexp to match object
compile(patten,flags=0)
'''

patten=r"(1(([35678]\d)|(47))\d{8})"
re_telephone=re.compile(patten)
print(re_telephone.match("13649284753"))
print(re_telephone.findall("13649284753xxx18191333449"))