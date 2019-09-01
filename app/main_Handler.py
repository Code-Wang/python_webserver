# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../source/html/index.html',)
        conn = comm.mysql.OperateDataBase()
        conn.conDB()

    def post(self):
        import time
        title = self.get_argument("title", None)
        content = self.get_argument("content", None)
        blog = dict()
        if title and content:
            blog["title"] = title
            blog["content"] = content
            blog["date"] = int(time.time())
            #coll = self.application.db.blog
            #coll.insert(blog)
            self.redirect("/blog")
        self.redirect("/")