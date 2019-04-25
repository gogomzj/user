import pymysql
pymysql.install_as_MySQLdb()

from app import create_app
from app import db

from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('develop')

# 一个app包含多个蓝本（blueprint），每一个蓝本都能处理自己的路由和视图和模板
# 用户登录的思路：
# 1.浏览器中有cookie 服务器会为每一浏览器保存一个session
# 2.用户把用户名和密码POST到服务器，服务器进行验证
# 3.如果用户名和密码验证通过，则在session中记录用户id和登录成功标志
# 4.把session id存放到浏览器的cookie中
# 5.以后浏览器在访问服务器，服务器从cookie中获取session id
# 6.然后服务器就知道是哪个用户在访问服务器了
# flask-login扩展封装了用户登录时候的一些操作，比如说对session和cookie的操作
# login_user(user)
# logout_user(user)
# User模型必须要提供四个方法：
# is_authenticated   is_active  is_anonymous  get_id
# UserMixin恰好提供了这四个方法

manager = Manager(app)

migrate = Migrate(app=app, db=db)

# 为数据库迁移添加命令db
manager.add_command('db', MigrateCommand)

from app.models import User
# 为manager添加系统初始化命令 python run.py init
@manager.command
def init() :
    user = User.query.filter_by(email='xxxx@xxxx.com').first()
    if user is None :
        user = User(name='gogomzj', email='xxxx@xxxx.com')
        user.confirmed = True
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

# 运行manager app的运行有manager接管
manager.run()

# app.run()