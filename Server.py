# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import os
import logging

import tornado.log
import tornado.ioloop
import tornado.web
import tornado.options

from loghandler import log_request


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


settings = {
    "cookie_secret": "md2html_server",
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "static_url_prefix": os.path.dirname(__file__),
    # "log_function": log_request,
}

handlers = [
    (r"/", MainHandler),
]
from route import handlers as ext_handlers
handlers.extend(ext_handlers)


def make_app():
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":

    tornado.options.parse_command_line()

    # from loghandler import self_log_request
    # self_log_request()

    logging.info("Server start...")

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()