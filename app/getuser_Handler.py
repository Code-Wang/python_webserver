# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class GetUserHandler(BaseHandler):
    def post(self):
        pageIndex = self.get_argument("index")
        pageCount = self.get_argument("count")
        conn = comm.mysql.OperateDataBase()
        sql = "select * from user_info order by id limit " + pageIndex + "," + pageCount
        result = conn.query(sql)
        userlist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['username'] = result['UserName'][i]
            dict['truename'] = result['TrueName'][i]
            dict['password'] = result['Password'][i]
            userlist.append(dict)
        self.write(json_encode(userlist))

