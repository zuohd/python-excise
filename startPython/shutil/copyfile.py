import shutil
# shutil.copyfileobj(open('old.txt','r'),open('new.txt','w'))
# shutil.copyfile('old.txt','new.txt')
shutil.copystat('old.txt','new.txt')
import os
# os.system('cat old.txt new.txt')
# os.system('ls -l old.txt new.txt')
os.system('stat old.txt new.txt')