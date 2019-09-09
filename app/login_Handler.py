# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql

class LoginHandler(tornado.web.RequestHandler):
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
        userName = self.get_argument("userName")
        passWord = self.get_argument("password")
        code = {}
        conn = comm.mysql.OperateDataBase()
        sql = "select Password from user_info where UserName = '" + userName + "'"
        result = conn.query(sql)
        if len(result) == 0:
            code['code'] = -1
        else:
            result = result['Password'][0]
            if result == passWord:
                code['code'] = 1
            else :
                code['code'] = -2
        self.write(json_encode(code))

