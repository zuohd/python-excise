import tornado.web
import tornado.ioloop
import tornado.httpserver  # import tornado httpserver module


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server.")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    # initiate a httpserver instance
    httpserver =tornado.httpserver.HTTPServer(app)
    httpserver.listen(8000)

    tornado.ioloop.IOLoop.current().start()
