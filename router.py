from app.account_Handler import AccountHandler 
from app.managerlogin_Handler import ManagerLoginHandler 
from app.getuser_Handler import GetUserHandler
from app.updateaccount_Handler import UpdateAccountHandler

routers = [
    (r'/managerlogin', ManagerLoginHandler),
    (r'/getaccountinfo', AccountHandler),
    (r'/getuserinfo', GetUserHandler),
    (r'/updateaccount', UpdateAccountHandler),
    ]