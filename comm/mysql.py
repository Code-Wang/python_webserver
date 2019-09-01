# -*- coding: utf-8 -*-
import pymysql
from .config import getConfig

class OperateDataBase ():
    def __init__(self):
        pass

    def conDB(self):
        id = 0
        name = "test_user"
        password = "123456"
        # 连接database
        conn = pymysql.connect(host=getConfig('db','host'), user=getConfig('db','username'),password=getConfig('db','password'),database=getConfig('db','dbname'),charset="utf8")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        cursor.execute("insert into user_info (id,name,password)"
                    " VALUES (\'%d\', \'%s\',\'%s\')" % (id, name, password))
        conn.commit()
        cursor.close()
        conn.close()
