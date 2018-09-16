import os


def getAllDir(path, sp=""):
    filesList = os.listdir(path)
    # print(filesList)
    sp += " "
    for filename in filesList:
        fpath = os.path.join(path, filename)
        if os.path.isdir(fpath):
            print(sp + "dir:" + filename)
            getAllDir(fpath,sp)
        else:
            print(sp + "file:" + filename)


getAllDir("/home")
