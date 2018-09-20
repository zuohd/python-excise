import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# define parameter,like --port=9000 list=a,b,c,de,
tornado.options.define("port", default=8000, type=None)
tornado.options.define("list", default=[], type=str, multiple=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server.")


if __name__ == '__main__':
    tornado.options.options.logging = None  # turn off logging
    tornado.options.parse_config_file("config")
    print(tornado.options.options.list)
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)

    # use parameter value
    httpserver.bind(tornado.options.options.port)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
