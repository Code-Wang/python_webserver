from app.account_Handler import AccountHandler 
from app.managerlogin_Handler import ManagerLoginHandler 
from app.getuser_Handler import GetUserHandler 

routers = [
    (r'/managerlogin', ManagerLoginHandler),
    (r'/getaccountindo', AccountHandler),
    (r'/getuserinfo', GetUserHandler),
    ]