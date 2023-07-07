import tornado.ioloop
import tornado.web
from tornado.options import define, options

from apps.main.urls import urls
from settings import settings

define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)

if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    print(f"Starting server on http://127.0.0.1:{options.port}")

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStopping server.")
