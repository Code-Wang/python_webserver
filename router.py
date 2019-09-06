from app.test_Handler import TestHandler 
from app.login_Handler import LoginHandler 


routers = [
    (r'/login', LoginHandler),
    (r'/test', TestHandler),
    ]