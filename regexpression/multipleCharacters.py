import re

r'''

(xyz) match "xyz" as the whole part
x? match zero or one x

x* match any number x
x+ match at least one x

x{n} match n number x

x{n,} match at least n number x

x{n,m} match at least n number and max number is m (n<=m)

x|y match x or y
'''

print(re.findall(r"(soderberg)","soderbergberg is soderberg man"))

print(re.findall(r"s?","ssoderbergberg is sssoderberg man"))

print(re.findall(r"s*","ssoderbergberg is sssoderberg man"))

print(re.findall(r"s+","ssoderbergberg is sssoderberg man"))

print(re.findall(r"a{3}","aaaabbaa"))

print(re.findall(r"a{3,}","aaaabbaaa"))
print(re.findall(r"a{3,5}","aaaabbaaa"))

print(re.findall(r"a|A","aaaabbAAA"))

