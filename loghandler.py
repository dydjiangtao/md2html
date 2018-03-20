# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-


import os
import re
import logging
# import commands
from tornado.log import access_log
from tornado.log import LogFormatter
from tornado.log import enable_pretty_logging

def process_info():
    pid = os.getpid()
    res = commands.getstatusoutput('ps aux|grep '+str(pid))[1].split('\n')[0]

    p = re.compile(r'\s+')
    l = p.split(res)
    info = {'user': l[0],
            'pid': l[1],
            'cpu': l[2],
            'mem': l[3],
            'vsa': l[4],
            'rss': l[5],
            'start_time': l[8]}
    # access_log.info(info)
    return info


def log_request(handler):
    """Writes a completed HTTP request to the logs.

    By default writes to the python root logger.  To change
    this behavior either subclass Application and override this method,
    or pass a function in the application settings dictionary as
    ``log_function``.
    """
    request_status = handler.get_status()
    request_summary = handler._request_summary()
    request_time = 1000.0 * handler.request.request_time()  # 1ms

    if handler.request.path == '/health':
        return
    if request_status < 400:
        log_method = access_log.info
    elif request_status < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error

    log_method("%d %s %.2fms", request_status, request_summary, request_time)


def log_request_with_UA(handler):
    """Writes a completed HTTP request to the logs.

    By default writes to the python root logger.  To change
    this behavior either subclass Application and override this method,
    or pass a function in the application settings dictionary as
    ``log_function``.
    """
    request_status = handler.get_status()
    request_summary = handler._request_summary()
    request_time = 1000.0 * handler.request.request_time()  # 1ms
    request_user_agent = handler.request.headers.get("User-Agent")

    if handler.request.path == '/health':
        return
    if request_status < 400:
        log_method = access_log.info
    elif request_status < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error

    log_method("%d %s %.2fms %s", request_status, request_summary, request_time, request_user_agent)


def self_log_request():
    logger = logging.getLogger()
    # logger.setLevel(logging.INFO)

    formatter = LogFormatter(
            # fmt='[%(asctime)s]%(color)s[%(levelname)s]%(end_color)s[(module)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
    )
    enable_pretty_logging(logger=logger)
    logger.handlers[0].setFormatter(fmt=formatter)
