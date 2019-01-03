import shutil
import os
print(os.getcwd())
shutil.make_archive(os.path.join(os.getcwd(),'tarfolder'),'gztar',root_dir=os.getcwd())