from app.test_Handler import TestHandler 
from app.managerlogin_Handler import ManagerLoginHandler 
from app.getuser_Handler import GetUserHandler 

routers = [
    (r'/managerlogin', ManagerLoginHandler),
    (r'/test', TestHandler),
    (r'/getuserinfo', GetUserHandler),
    ]