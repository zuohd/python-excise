import tornado.web
import config
import os
from models import Student

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
    def initialize(self):
        print("initialize")

    def prepare(self):
        print("prepare")

    def set_default_headers(self):
        print("set_default_headers")

    def write_error(self, status_code, **kwargs):
        print("write_error")

    def get(self, *args, **kwargs):
        print("Http request-get")
        self.write("I'm the first line")
        self.write("I'm the seconde line")
        self.write("I'm the third line")
        self.finish()  # refresh buffer and close current request channel
        # self.write("I'm the forth line")  # after finish method,write won't work

    def on_finish(self):
        print("on_finish ")


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
        name = self.get_body_argument("username")
        password = self.get_body_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        print(name, password, hobbyList)
        self.write("ok")


class ZhuyinHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.body)
        print(self.request.headers)
        print(self.request.remote_ip)
        print(self.request.files)
        print("output request object property values")


class UploadFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upfile.html")

    def post(self, *args, **kwargs):
        files = self.request.files
        # print(files)
        for inputname in files:
            fileArr = files[inputname]
            for fileObj in fileArr:
                # save into file path
                filepath = os.path.join(config.BASE_DIRS, 'upfile/' + fileObj.filename)
                with open(filepath, "wb") as f:
                    f.write(fileObj.body)

        self.write("ok")


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "Soderberg",
            "age": 34
        }
        flag = 1

        students = [per, {"name": "Jack", "age": 78}]
        self.render("home.html", num=temp, **per, flag=flag, students=students)


class FunctionHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def add(n1, n2):
            return n1 + n2

        self.render("home.html", add=add)


class EscapeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<a href='baidu.com'>link</a>"
        self.render("escape.html", str=str)


class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        title = "cart page"
        self.render("cart.html", title=title)


class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # stu=Student("Rose",50)
        # stu.save()
        # self.write("ok")
        students = Student.all()
        print(students)
        self.render("students.html", students=students)
