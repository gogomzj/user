from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 导入配置字典
from config import config

# 创建数据库访问对象
db = SQLAlchemy()

# 创建发送邮件对象
mail = Mail()

# 创建login_manger对象  实现对用户登录登出的控制（session和cookie）
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# 有些视图函数（路由）必须是登录用户才能，如果未登录的用户访问的话我们给他重定向到登录路由
# 如果未登录用户访问了需要登录才能访问的路由那么自动重定向到auth蓝本login视图函数
login_manager.login_view = 'auth.login'

# 创建app的函数
def create_app(config_name) :
    # 创建app
    app = Flask(__name__)

    #加载配置
    app.config.from_object(config[config_name])

    # 初始化
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app