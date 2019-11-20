from app.account_Handler import AccountHandler 
from app.managerlogin_Handler import ManagerLoginHandler 
from app.getuser_Handler import GetUserHandler
from app.updateaccount_Handler import UpdateAccountHandler
from app.updateuser_Handler import UpdateUserHandler
from app.statics_Handler import StaticsHandler
from app.delaccount_Handler import DelAccountHandler

routers = [
    (r'/managerlogin', ManagerLoginHandler),
    (r'/getaccountinfo', AccountHandler),
    (r'/getuserinfo', GetUserHandler),
    (r'/updateuser', UpdateUserHandler),
    (r'/updateaccount', UpdateAccountHandler),
    (r'/delaccount', DelAccountHandler),
    (r'/getstatics',StaticsHandler),
    ]