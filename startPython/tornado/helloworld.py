import tornado.ioloop
import tornado.web
import MemcacheToSession

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session=MemcacheToSession.Session(self)

class MainHandler(BaseHandler):
    def get(self):
        Info=self.session.GetAll()
        self.render("template/index.html",Data=Info)
        # self.write("Hello, world")
    def post(self, *args, **kwargs):
        Key=self.get_argument('key')
        Val=self.get_argument('val')
        action=self.get_argument('action')
        if action=='set':
            self.session[Key]=Val
        elif action=='del':
            del self.session[Key]

        Info=self.session.GetAll()
        self.render('template/index.html',Data=Info)
settings={
    # 'template_path':'template',
    'cookie_secret':'508CE6152CB93994628D3E99934B83CC'
}
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()