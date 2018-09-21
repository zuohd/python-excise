import tornado.web

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("hello customer server from config.py file.")
        url=self.reverse_url("hello")
        self.write("<a href='%s'>open a page</a>"%(url))


class SoderbergHandler(RequestHandler):
    def initialize(self, age, number):
        self.age = age
        self.number = number

    def get(self, *args, **kwargs):
        self.write("yes,we can.%d-%s" % (self.age, self.number))


import json


class Json1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "Jack",
            "age": 45,
            "height": 175,
            "weight": 80
        }
        jsonStr = json.dumps(per)
        self.set_header("Content-Type", "application/json;charset=utf-8")
        self.set_header("name", "xxxx")
        self.write(jsonStr)


class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "Jack",
            "age": 45,
            "height": 175,
            "weight": 80
        }
        self.write(per)


class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/html;charset=utf-8")

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


class StatusHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)
        self.write("********************")


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")


class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            # 500 page
            self.write("server internal error")
        elif status_code == 404:
            # 404 page
            self.write("Not found")
        else:
            self.write("don't know")
        self.set_status(status_code)

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == '0':
            self.send_error(500)
        self.write("right.")


class HelloHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("aaa")
