import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import WebSocketHandler

from tornado.web import RequestHandler


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('chat.html')


class ChatHandler(WebSocketHandler):
    users = []

    def open(self):
        self.users.append(self)
        for user in self.users:
            user.write_message(u"[%s] logined" % (self.request.remote_ip))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message(u"[%s] logout" % (self.request.remote_ip))

    def on_message(self, message):
        for user in self.users:
            user.write_message(u"[%s] say:%s" % (self.request.remote_ip, message))

    def check_origin(self, origin):
        return True
