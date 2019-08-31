from app.test_Handler import TestHandler 
from app.main_Handler import MainHandler 


routers = [
    (r'/', MainHandler),
    (r'/test', TestHandler),
    ]