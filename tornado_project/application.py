import os

import tornado.web
from views import index
import config
from ORM.mysqlclass import  MysqlConnect


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r'/', index.IndexHandler),
            (r'/soderberg', index.SoderbergHandler, {"age": 30, "number": "123456"}),
            tornado.web.url(r'/hello', index.HelloHandler, name="hello"),  # reverse proxy,paramter name can't change
            (r'/json1', index.Json1Handler),
            (r'/json2', index.Json2Handler),
            (r'/header', index.HeaderHandler),
            (r'/status', index.StatusHandler),
            (r'/index', index.RedirectHandler),
            # iseror?flag=0
            (r'/iserror', index.ErrorHandler),
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.liuyifeiHandler),
            # (r'/liuyifei/(?p<p1>\w+)/(?p<p3>\w+)/(?p<p2>\w+)', index.liuyifeiHandler),
            (r'/zhangmanyu', index.ZhangmanyuHandler),
            (r'/postfile', index.PostfileHandler),
            (r'/zhuyin', index.ZhuyinHandler),
            (r'/uploadfile', index.UploadFileHandler),
            (r'/home', index.HomeHandler),
            (r'/function', index.FunctionHandler),
            (r'/escape', index.EscapeHandler),
            (r'/cart', index.CartHandler),
            (r'/students',index.StudentsHandler),
            (r'/commoncookie',index.CommonCookieHandler),
            (r'/secretcookie',index.SecretCookieHandler),
            #cookie couter-record browser visit times
            (r'/cookiecounter',index.CookieCounterHandler),
            # staticFileHandler,should be the end of all routes
            (r'/(.*)$', index.StaticFileHandler,
             {"path": os.path.join(config.BASE_DIRS, "static/html"), "default_filename": "index.html"})

        ]
        super(Application, self).__init__(handlers, **config.settings)
        # self.db=MysqlConnect(config.mysql["host"],config.mysql["user"],config.mysql["password"],config.mysql["dbName"])
