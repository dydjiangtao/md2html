# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


from tornado.web import url

from handler import post


handlers = [
    url(r"/post", post.PostHandler),
]
