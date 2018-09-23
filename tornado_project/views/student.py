import tornado.web
from tornado.httpclient import AsyncHTTPClient
import time
import json

from tornado.web import RequestHandler


class CallbackStudentsHandler(RequestHandler):
    def on_response(self, response):
        print("**************")
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
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


class CoroutineStudentsHandler(RequestHandler):
    @tornado.web.gen.coroutine
    def get(self, *args, **kwargs):
        url = "https://jsonplaceholder.typicode.com/comments"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(str(data))


class RefineCoroutineStudentsHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(str(res))

    @tornado.gen.coroutine
    def getData(self):
        url = "https://jsonplaceholder.typicode.com/comments"
        client = AsyncHTTPClient()
        result = yield client.fetch(url)
        if result.error:
            ret={"ret":0}
        else:
            ret=json.loads(result.body)
        raise tornado.gen.Return(ret)
