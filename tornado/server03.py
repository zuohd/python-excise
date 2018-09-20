import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# define parameter
tornado.options.define("port", default=8000, type=None)
tornado.options.define("list", default=[], type=str)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello customer server.")


if __name__ == '__main__':
    # convert command arguments  and save into tornado.options object
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    httpserver = tornado.httpserver.HTTPServer(app)
    # use parameter value
    httpserver.bind(tornado.options.options.port)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
