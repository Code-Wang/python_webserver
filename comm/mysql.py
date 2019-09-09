# -*- coding: utf-8 -*-
import pymysql
import pandas
from .config import getConfig

class OperateDataBase ():
    def __init__(self):
        pass

    def execute(self, sql):
        # 连接database
        conn = pymysql.connect(host=getConfig('db','host'), user=getConfig('db','username'),password=getConfig('db','password'),database=getConfig('db','dbname'),charset="utf8")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def query(self, sql):
        # 连接database
        conn = pymysql.connect(host=getConfig('db','host'), user=getConfig('db','username'),password=getConfig('db','password'),database=getConfig('db','dbname'),charset="utf8")
        # 得到一个可以执行SQL语句的光标对象
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        """
        data=pandas.read_sql(sql,conn)
        conn.close()
        return data

