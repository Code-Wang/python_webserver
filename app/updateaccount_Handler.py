# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class UpdateAccountHandler(BaseHandler):
    def post(self):
        Id = int(self.get_argument("id"))
        Webset = self.get_argument("webset")
        Account = self.get_argument("account")
        Password = self.get_argument("password")
        AccountName = self.get_argument("accountname")
        Telphone = self.get_argument("telphone")
        Address = self.get_argument("address")
        PayType = self.get_argument("paytype")
        PayAccount = self.get_argument("payaccount")
        DefaultSize = float(self.get_argument("defaultsize"))

        conn = comm.mysql.OperateDataBase()
        sql = "update account_info " \
                "SET Webset=\'%s\' , Account=\'%s\' , Password=\'%s\' , Accountname=\'%s\' , Telphone=\'%s\' , Address=\'%s\' , PayType=\'%s\' , " \
                    "PayAccount=\'%s\' , DefaultSize=%f " % (Webset, Account, Password, AccountName, Telphone, Address, PayType, PayAccount, DefaultSize)

        if Id != 0:
            condition = "where Id=%d" % (Id)
            sql += condition

        print(sql)
        result = conn.execute(sql)
        print(result)
        if not result:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        else:
            rspStr = json_encode({'code': 0, 'desc': "update success"})
        self.write(rspStr)

