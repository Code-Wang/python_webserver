# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql
from tornado.escape import json_encode
from app.base_Handler import BaseHandler

class DelAccountHandler(BaseHandler):
    def post(self):
        Id = str(self.get_argument("id"))
        conn = comm.mysql.OperateDataBase()
        sql = "DELETE FROM account_info WHERE Id = " + Id

        conn = comm.mysql.OperateDataBase()
        result = conn.execute(sql)

        if not result:
            rspStr = json_encode({'code': 0, 'desc': "delete success"})
        else:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        self.write(rspStr)

