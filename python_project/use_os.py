import os  # Acess os features

print(os.name)
print(os.uname())  # machine info
print(os.environ)  # environment variable
print(os.environ.get("PATH"))

print(os.curdir)  # current path
print(os.getcwd())  # current work path
print(os.listdir())  # list all files and dir in current work path
# os.mkdir("soderberg")
# os.rmdir(".\soderberg")
print(os.stat("soderberg"))
# os.remove("testfile") #remove file
# os.system("ipython")
print(os.path.abspath("."))