'''
read file operation steps:
1.open file
open(path,flag[,encoding,errors])
flag:
r   read-only open,file description on the file header
rb  binnary format open as read only
r+  open a file to be read and write
w   open a file to be write only,and overwrite the existed file,otherwise new a file
wb  write binnary formate data to open a file
w+
a   open a file to append file content
a+

error:error handling,ignore is ignore errors
2.read file content
<1>read all content:str1=f.read()
<2>str2=f.read(10)
<3>str3=f.readline()
<4>list1=f.readlines()
3.close file
'''
try:
    f1=open("test.py","r",encoding="utf-8",errors="ignore")
    # str1=f1.read(10)
    # str2=f1.readline()
    list1=f1.readlines();
    print(list1)
    f1.seek(0) #modify the description position

    str=f1.read()
    print(str)
finally:
    if f1:
        f1.close()

with open("test.py","r") as f2:
    content=f2.read()
    print(content)