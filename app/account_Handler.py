# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql
from app.base_Handler import BaseHandler

class AccountHandler(BaseHandler):
    def post(self):
        pageIndex = self.get_argument("index")
        pageCount = self.get_argument("count")
        conn = comm.mysql.OperateDataBase()
        sql = "select * from account_info order by id limit " + pageIndex + "," + pageCount
        result = conn.query(sql)
        userlist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['webset'] = result['Webset'][i]
            dict['account'] = result['Account'][i]
            dict['password'] = result['Password'][i]
            dict['accountname'] = result['Accountname'][i]
            dict['telphone'] = result['Telphone'][i]
            dict['address'] = result['Address'][i]
            dict['paytype'] = result['PayYype'][i]
            dict['payaccount'] = result['PayAccount'][i]
            dict['defaultsize'] = result['DefaultSize'][i]
            dict['state'] = result['State'][i]
            userlist.append(dict)
        self.write(json_encode(userlist))

