import os


# Deep traverse with stack-DFS
def getAllDirDeep(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)
        for filename in filesList:
            fileAbsPath = os.path.join(dirPath, filename)
            if os.path.isdir(fileAbsPath):
                print("Directory:" + filename)
                stack.append(fileAbsPath)
            else:
                print("File:" + filename)


getAllDirDeep("/home")
