import re

a = re.match("a.c", 'abc').group()
print(a)

b=re.match('\d','3').group()
print(b)

c=re.match('\D','a').group()
print(c)

e=re.match('\s',' ').group()
print(e)

f=re.match('\S','abc').group()
print(f)

g=re.match('[hell]?','hellhello').group()
print(g)
