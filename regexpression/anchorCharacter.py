import re
r'''
^  begin of line match,it's not the same as in []
$  end of line match

\A match begin of string(first line)

\Z match end of string(first line)

\b match word edge ,"er\b" match never but not nerve
\B match non word edge,oppsit as "\b"
'''

print(re.findall("good$","soderberg is good"))
print(re.findall("^soderberg","soderberg is a good man\nsoderberg is a good man",re.M))
print(re.search("^soderberg$","soderberg"))

print(re.findall("\Asoderberg","soderberg is a good man\nsoderberg is a good man",re.M))
