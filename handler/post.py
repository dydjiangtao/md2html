# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


from handler.base_handler import BaseRequestHandler
from utils.md2html import md2html


class PostHandler(BaseRequestHandler):

    """get all post"""

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        post_path = self.static_url('/static/post/2018-03-19-文档.md', include_version=False)
        with open(post_path, 'rb') as f:
            post = f.read()

        if post:
            post = post.decode()
        else:
            post = '暂无'

        post = md2html(post)

        self.write(post)
        return
