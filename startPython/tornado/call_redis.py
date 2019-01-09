import tornado.ioloop
import tornado.web
import time
import redis

pool = redis.ConnectionPool(host='192.168.1.143', port=6379)
conn = redis.Redis(connection_pool=pool)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        CurrentTime = conn.get('curt')
        if CurrentTime:
            self.write(CurrentTime)
        else:
            CurrentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            conn.set('curt', CurrentTime, ex=5)
            self.write(CurrentTime)


settings = {
    "template_path": "template"
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == '__main__':
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
