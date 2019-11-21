# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class GetUserHandler(BaseHandler):
    def get(self):
        conn = comm.mysql.OperateDataBase()
        sql = "select count(*) as count from user_info"
        result = conn.query(sql)
        data = {'Count' : str(result['count'][0])}
        print(data)
        self.write(json_encode(data))

    def post(self):
        pageIndex = int(self.get_argument("index"))
        pageCount = int(self.get_argument("count"))
        beginIndex = str(pageIndex * pageCount)
        endIndex = str((pageIndex + 1)  * pageCount)
        conn = comm.mysql.OperateDataBase()
        sql = "select * from user_info order by id limit " + beginIndex + "," + endIndex
        result = conn.query(sql)
        userlist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['id'] = str(result['Id'][i])
            dict['username'] = result['UserName'][i]
            dict['truename'] = result['TrueName'][i]
            dict['password'] = result['Password'][i]
            userlist.append(dict)
        self.write(json_encode(userlist))

