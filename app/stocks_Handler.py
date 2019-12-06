# -*- coding: utf-8 -*-
import tornado.web
from tornado.escape import json_encode
import comm.mysql
from app.base_Handler import BaseHandler

class GetStocksHandler(BaseHandler):
    def post(self):
        conn = comm.mysql.OperateDataBase()
        sql = "select * from stocks_info"
        result = conn.query(sql)
        itemlist = []
        length = len(result['Id'])
        for i in range(0, length):
            dict = {}
            dict['itemindex'] = str(result['Id'][i])
            dict['itemid'] = str(result['ItemId'][i])
            dict['itemname'] = result['ItemName'][i]
            dict['itemimage'] = result['ItemImage'][i]
            dict['itemcount'] = str(result['ItemCounts'][i])
            itemlist.append(dict)
        self.write(json_encode(itemlist))

