import tornado.web
from tornado.httpclient import AsyncHTTPClient
import time
import json

from tornado.web import RequestHandler


class StudentsHandler(RequestHandler):
    def on_response(self, response):
        print("**************")
        if response.error:
            self.send_error(500)
        else:
            data=json.loads(response.body)
            self.write(str(data))
        self.finish()

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        # time.sleep(30)
        url = "https://jsonplaceholder.typicode.com/comments"
        # create client
        client = AsyncHTTPClient()
        client.fetch(url, self.on_response)
        self.write("ok")


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("home")
