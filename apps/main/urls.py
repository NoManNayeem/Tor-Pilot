from tornado.web import URLSpec as url
from .views import HomeHandler

urls = [
    url(r"/", HomeHandler),
]
