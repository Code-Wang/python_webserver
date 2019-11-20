# -*- coding: utf-8 -*-
import tornado.web
import comm.mysql
from tornado.escape import json_encode
from app.base_Handler import BaseHandler

class AccountHandler(BaseHandler):
    def get(self):
        conn = comm.mysql.OperateDataBase()
        sql = "select count(*) as count from account_info"
        result = conn.query(sql)
        dict = {}
        dict['Count'] = result['count']
        self.write(json_encode(dict))

    def post(self):
        pageIndex = self.get_argument("index")
        pageCount = self.get_argument("count")
        conn = comm.mysql.OperateDataBase()
        sql = "select * from account_info order by id limit " + pageIndex*pageCount + "," + (pageIndex + 1)*pageCount
        result = conn.query(sql)
        accountlist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['id'] = str(result['Id'][i])
            dict['webset'] = result['Webset'][i]
            dict['account'] = result['Account'][i]
            dict['password'] = result['Password'][i]
            dict['accountname'] = result['Accountname'][i]
            dict['telphone'] = result['Telphone'][i]
            dict['address'] = result['Address'][i]
            dict['paytype'] = result['PayType'][i]
            dict['payaccount'] = result['PayAccount'][i]
            dict['defaultsize'] = str(result['DefaultSize'][i])
            dict['state'] = str(result['State'][i])
            accountlist.append(dict)
        self.write(json_encode(accountlist))

