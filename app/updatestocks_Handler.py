# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class UpdateStocksHandler(BaseHandler):
    def post(self):
        Operate = self.get_argument("operate")
        SalersManName = self.get_argument("salersmanname")
        ItemId = self.get_argument("itemid")
        ItemName = self.get_argument("itemname")
        ItemCounts = int(self.get_argument("counts"))
        Price = float(self.get_argument("price"))
        TotalPrice = float(self.get_argument("totalprice"))
        CustomerName = self.get_argument("customername")
        CustomerTelphone = self.get_argument("customertelphone")
        CustomerAddress = self.get_argument("customeraddress")
        Date = self.get_argument("date") 

        sql = ""
        if (Operate == "sell"):
            self.add_sales_data()
            sql = "update stocks_info " \
                "SET ItemCounts=ItemCounts - %d where ItemId=\'%s\'" % (ItemCounts, ItemId) 
        elif (Operate == "stocks"):
            self.add_stcoks_data()
            sql = "update stocks_info " \
                "SET ItemCounts=ItemCounts + %d where ItemId=\'%s\'" % (ItemCounts, ItemId) 
        else:
            rspStr = json_encode({'code': 1, 'desc': "undefine operate"})
            self.write(rspStr)
            return

        conn = comm.mysql.OperateDataBase()
        result = conn.execute(sql)
        if not result:
            rspStr = json_encode({'code': 0, 'desc': "update success"})
        else:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        self.write(rspStr)

    def add_sales_data(self):
        SalersManName = self.get_argument("salersmanname")
        ItemId = self.get_argument("itemid")
        ItemName = self.get_argument("itemname")
        ItemCounts = int(self.get_argument("counts"))
        Price = float(self.get_argument("price"))
        TotalPrice = float(self.get_argument("totalprice"))
        CustomerName = self.get_argument("customername")
        CustomerTelphone = self.get_argument("customertelphone")
        CustomerAddress = self.get_argument("customeraddress")
        Date = self.get_argument("date") 

        sql = "insert into sales_data (Index, SalersManName, ItemId, ItemName, ItemCounts, Price, TotalPrice, CustomerName, CustomerTelphone, CustomerAddress, Date)" \
            "VALUES (0, \'%s\' ,\'%s\' ,\'%s\' ,%d ,%f ,%f ,\'%s\' ,\'%s\' ,\'%s\' ,\'%s\')" % (SalersManName, ItemId, ItemName, ItemCounts, Price, TotalPrice, CustomerName, CustomerTelphone, CustomerAddress, Date)

        conn = comm.mysql.OperateDataBase()
        result = conn.execute(sql)
        if not result:
            rspStr = json_encode({'code': 0, 'desc': "update success"})
        else:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        self.write(rspStr)
    
    def add_stocks_data(self):
        ItemId = self.get_argument("itemid")
        ItemName = self.get_argument("itemname")
        ItemCounts = int(self.get_argument("counts"))
        Price = float(self.get_argument("price"))
        TotalPrice = float(self.get_argument("totalprice"))
        Date = self.get_argument("date") 

        sql = "insert into stocks_data (Index, ItemId, ItemName, ItemCounts, Price, TotalPrice, Date)" \
            "VALUES (0, \'%s\' ,\'%s\' ,%d ,%f ,%f ,\'%s\')" % (ItemId, ItemName, ItemCounts, Price, TotalPrice, Date)

        conn = comm.mysql.OperateDataBase()
        result = conn.execute(sql)
        if not result:
            rspStr = json_encode({'code': 0, 'desc': "update success"})
        else:
            rspStr = json_encode({'code': 1, 'desc': "database exception"})
        self.write(rspStr)