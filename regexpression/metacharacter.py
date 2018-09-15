import re


r'''
. match any characters except \n
[0123456789] match any digits characters
[abcde] match any included lettes character
[a-z] any lowed case letter
[A-Z] any uppercase letter
[0-9] the same as [0123456789]
[0-9a-zA-Z] any letters and digit character

[0-9a-zA-Z_] any letter\digit\under line

[^soderberg] any characters except soderberg,^ is tuozi fu

[^0-9] any not digit character

\d any digit,the same as [0-9]

\D any not digit character,the same as [^9]

\w the same as [0-9a-zA-Z_]

\W the sam as [^0-9a-zA-Z_]

\s any space/ enter/another line/page/tab character,the same as [ \f\n\r\t]

\S the same as [^ \f\n\r\t]

'''


print(re.findall("\w","soderberg is a good man 3"))