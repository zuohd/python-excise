import os
BASE_DIRS=os.path.dirname(__file__)
# parameter

options = {
    "port": 8085
}

# configuration
settings = {
    "static_path":os.path.join(BASE_DIRS,"static"),
    "template_path":os.path.join(BASE_DIRS,"templates"),
    "debug":True,
    # "autoreload":True
}
