import os
import collections

# breadth traverse with queue-BFS

def getAllDirBFS(path):
    queue=collections.deque()
    queue.append(path)
    while len(queue)!=0:
        dirPath=queue.popleft()
        filesList=os.listdir(dirPath)
        for filename in filesList:
            fileAbsPath=os.path.join(dirPath,filename)
            if os.path.isdir(fileAbsPath):
                print("Directory: "+filename)
                queue.append(fileAbsPath)
            else:
                print("File:"+filename)
                



getAllDirBFS("/home")