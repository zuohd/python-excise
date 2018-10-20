import tornado.web  # basic web framework
import tornado.ioloop  # core io loop module,wrap epoll and BSD kqueue


class IndexHandler(tornado.web.RequestHandler):
    # Handle get request
    def get(self, *args, **kwargs):
        # correspond to http request method and response to web browser
        self.write("hello .This is a test")


if __name__ == '__main__':
    # initiate an app object
    # Application:core application class  of tornado web,match server interface
    # Being stored the route mapping table and there ia s listen mehod to create an http server instance
    # and binding port
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    # binding listen port,here server is not listening yet
    app.listen(8000)


    '''
    IOLoop.current():return current thread IOLoop instance
    IOLoop.start():start I/O loop of IOLoop instance while start listening
    '''
    tornado.ioloop.IOLoop.current().start()
