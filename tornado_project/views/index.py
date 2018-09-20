import tornado.web

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server from config.py file.")


class SoderbergHandler(RequestHandler):
    def initialize(self, age, number):
        self.age = age
        self.number = number

    def get(self, *args, **kwargs):
        self.write("yes,we can.%d-%s"%(self.age,self.number))
