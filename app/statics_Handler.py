# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql
from tornado.escape import json_encode
from app.base_Handler import BaseHandler

class StaticsHandler(BaseHandler):
    def post(self):
        pageIndex = self.get_argument("index")
        pageCount = self.get_argument("count")
        conn = comm.mysql.OperateDataBase()
        sql = "SELECT Webset,COUNT(*) as Count FROM account_info GROUP BY Webset ORDER BY COUNT(*) desc"
        result = conn.query(sql)
        userlist = []
        length = len(result['Webset'])
        for i in range(0, length):
            dict = {}
            dict['webset'] = result['Webset'][i]
            dict['count'] = result['Count'][i]
            userlist.append(dict)
        self.write(json_encode(userlist))

