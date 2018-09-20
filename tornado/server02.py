import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server.")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpserver =tornado.httpserver.HTTPServer(app)
    # httpserver.listen(8000)
    httpserver.bind(8000)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
