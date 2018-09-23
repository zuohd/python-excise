import os

BASE_DIRS = os.path.dirname(__file__)
# parameter

options = {
    "port": 8086
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
    "cookie_secret":"oxylSN4KSyyku20NfX2ke/VoW5KDKkV6nr54TuCKGrs=",
    "xsrf_cookies":True,
    "login_url":"/login",
    # "autoescape": None
    # "autoreload":True

}
