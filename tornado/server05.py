import tornado.web
import tornado.ioloop
import tornado.httpserver
import config



class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server from config.py file.")


if __name__ == '__main__':
    print("list=",str(config.options["list"]))
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)

    # use parameter value
    httpserver.bind(config.options["port"])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
