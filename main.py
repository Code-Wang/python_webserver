# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
from router import routers

define('port', default=8002, help='run on the given port', type=int)


class Application(tornado.web.Application):
    def __init__(self): 
        handlers = routers
        tornado.web.Application.__init__(self, handlers)

    settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    debug=True,
    )

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()