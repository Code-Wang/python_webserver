# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql
from app.base_Handler import BaseHandler

class TestHandler(BaseHandler):
    def get(self):
        self.render('../source/html/test.html',)
        """
        conn = comm.mysql.OperateDataBase()
        sql = "select * from user_info"
        data = conn.query(sql)
        print(data)
        """


