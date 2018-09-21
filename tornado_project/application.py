import tornado.web
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/soderberg',index.SoderbergHandler,{"age":30,"number":"123456"}),
            (r'/json1',index.Json1Handler),
            (r'/json2', index.Json2Handler),
            (r'/header',index.HeaderHandler),
            (r'/status',index.StatusHandler),
            (r'/index',index.RedirectHandler),
            #iseror?flag=2
            (r'/iserror',index.ErrorHandler)
        ]
        super(Application, self).__init__(handlers,**config.settings)