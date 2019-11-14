# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
import time
from app.base_Handler import BaseHandler

class LoginHandler(BaseHandler):
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
        elif self.checkLoginTime(userName, conn):
            code['code'] = -3
        else:
            result = result['Password'][0]
            if result == passWord:
                self.resetFailTimes(userName, conn)
                code['code'] = 1
            else :
                self.increaseFailTimes(userName, conn)
                code['code'] = -2
        self.write(json_encode(code))

    def checkLoginTime(self, userName, conn):
        sql = "select * from login_failed where UserName = '" + userName + "'"
        result = conn.query(sql)
        if len(result) == 0:
            return False
        
        if int(result['failTimes'][0]) >= 5:
            if (int(result['lastFailedTime'][0])+ 900) < time.time():
                self.resetFailTimes(userName, conn)
                return False
            return True

        return False

    def increaseFailTimes(self, userName, conn):
        sql = "select * from login_failed where UserName = '" + userName + "'"
        result = conn.query(sql)
        if len(result) == 0 :
            insertSql = "insert into login_failed (userName, failTimes, lastFailedTime)" \
                " VALUES (\'%s\', '1',\'%d\')" % (userName, int(time.time()))
            conn.execute(insertSql)  
        else:
            FailTimes = int(result['failTimes'][0]) + 1
            updateSql = "update login_failed set failTimes = \'%d\' , lastFailedTime = \'%d\'where UserName = \'%s\'" % (FailTimes,int(time.time()),userName)
            conn.execute(updateSql)
        return

    def resetFailTimes(self, userName, conn):
        sql = "update login_failed set failTimes = 0 where UserName = '" + userName + "'"
        conn.execute(sql)
        return

