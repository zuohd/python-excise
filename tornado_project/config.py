import os

BASE_DIRS = os.path.dirname(__file__)
# parameter

options = {
    "port": 8085
}

#database config
mysql = {
    "host": "localhost",
    "user": "root",
    "password": "root123",
    "dbName": "study"
}
# configuration
settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    "debug": True,
    # "autoescape": None
    # "autoreload":True

}
