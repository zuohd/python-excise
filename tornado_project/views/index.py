import tornado.web

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("hello customer server from config.py file.")
        url = self.reverse_url("hello")
        self.write("<a href='%s'>open a page</a>" % (url))


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


class liuyifeiHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        self.write(h1 + "-" + h2 + "-" + h3)
        print("ok")


class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument("a")
        # alist=self.get_query_arguments("a")
        # print(alist[0],alist[1])
        b = self.get_query_argument("b", default="hello")
        c = self.get_query_argument("c", strip=False)
        self.write("zhangmanyu is beautiful,a=%s,b=%s,c=*%s*" % (a, b, c))


# Post
class PostfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')

    def post(self, *args, **kwargs):
       name=self.get_body_argument("username")
       password=self.get_body_argument("passwd")
       hobbyList=self.get_body_arguments("hobby")
       print(name,password,hobbyList)
       self.write("ok")
