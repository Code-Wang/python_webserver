# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class GetOrdersHandler(BaseHandler):
    def get(self):
        conn = comm.mysql.OperateDataBase()
        sql = "select count(*) as count from sales_data"
        result = conn.query(sql)
        data = {'Count' : str(result['count'][0])}
        self.write(json_encode(data))


    def post(self):
        pageIndex = int(self.get_argument("index"))
        pageCount = int(self.get_argument("count"))
        beginIndex = str(pageIndex * pageCount)
        endIndex = str((pageIndex + 1)  * pageCount)        
        conn = comm.mysql.OperateDataBase()
        sql = "select * from sales_data order by Id limit " + beginIndex + "," + endIndex     
        result = conn.query(sql)
        orderslist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['salersmanname'] = result['SalersManName'][i]
            dict['itemid'] = result['ItemId'][i]
            dict['itemname'] = result['ItemName'][i]
            dict['counts'] = str(result['ItemCounts'][i])
            dict['price'] = str(result['Price'][i])
            dict['totalprice'] = str(result['TotalPrice'][i])
            dict['customername'] = result['CustomerName'][i]
            dict['customertelphone'] = result['CustomerTelphone'][i]
            dict['customeraddress'] = result['CustomerAddress'][i]
            dict['date'] = result['Date'][i]
            orderslist.append(dict)
        self.write(json_encode(orderslist)) 