# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../source/html/test.html',)
        """
        conn = comm.mysql.OperateDataBase()
        sql = "select * from user_info"
        data = conn.query(sql)
        print(data)
        """


