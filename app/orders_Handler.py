# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class GetOrdersHandler(BaseHandler):
    def post(self):
        conn = comm.mysql.OperateDataBase()
        sql = "select * from sales_info"
        result = conn.query(sql)
        orderslist = []
        length = len(result['Index'])
        for i in range(0, length):
            dict = {}
            dict['salersmanname'] = str(result['SalersManName'][i])
            dict['itemid'] = str(result['ItemId'][i])
            dict['itemname'] = result['ItemName'][i]
            dict['counts'] = result['ItemCounts'][i]
            dict['price'] = str(result['Price'][i])
            dict['totalprice'] = str(result['TotalPrice'][i])
            dict['customername'] = str(result['CustomerName'][i])
            dict['customertelphone'] = str(result['CustomerTelphone'][i])
            dict['customeraddress'] = str(result['CustomerAddress'][i])
            dict['date'] = str(result['Date'][i])
            orderslist.append(dict)
        self.write(json_encode(orderslist))