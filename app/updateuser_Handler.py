# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class UpdateUserHandler(BaseHandler):
    def post(self):
        Id = int(self.get_argument("id"))
        UserName = int(self.get_argument("username"))
        TrueName = self.get_argument("truename")
        Password = self.get_argument("password")
        sql = ""

        if Id != 0:
            sql = "update user_info " \
                "SET UserName=\'%s\' , Account=\'%s\' , Password=\'%s\' where Id=%d" % (UserName, TrueName, Password, Id)
        else:
            sql = "insert into user_info (Id, UserName, TrueName, Password) " \
                    "VALUES (0, \'%s\' ,\'%s\' ,\'%s\')" % (UserName, TrueName, Password)

        print(sql)
        conn = comm.mysql.OperateDataBase()
        result = conn.execute(sql)
        if not result:
            rspStr = json_encode({'code': 0, 'desc': "update success"})
        else:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        self.write(rspStr)