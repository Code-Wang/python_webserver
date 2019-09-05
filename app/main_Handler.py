# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../source/html/login.html",)
        """
        conn = comm.mysql.OperateDataBase()
        id = 0
        name = "test"
        password = "123456"
        sql = "insert into user_info (id,name,password)" \
                " VALUES (\'%d\', \'%s\',\'%s\')" % (id, name, password)
        conn.execute(sql)
        """

    def post(self):
        pass