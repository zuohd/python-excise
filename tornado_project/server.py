import tornado.httpserver
import tornado.ioloop
import config
from application import Application

if __name__ == '__main__':
    app = Application()

    httpserver = tornado.httpserver.HTTPServer(app)

    httpserver.bind(config.options["port"])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()
