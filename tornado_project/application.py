import tornado.web
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/soderberg',index.SoderbergHandler,{"age":30,"number":"123456"})
        ]
        super(Application, self).__init__(handlers,**config.settings)
