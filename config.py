
class Config :
    # 表单
    WTF_CSRF_ENDABLED = True
    SECRET_KEY = 'iot.embsky.com'
    # 邮箱
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = '25'
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mzjbaby@sina.com'
    MAIL_PASSWORD = '19970206'
    # 数据库
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy将会追踪对象的修改并且发送信号。
    # 注意:这需要额外的内存，如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 自定义
    BLOG_PER_COUNT = 5

class DevelopConfig(Config) :
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/dev_project'

class TestConfing(Config) :
    TEST = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/test_project'

class ProductConfing(Config) :
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/product_project'

config = {
    'develop':DevelopConfig,
    'test':TestConfing,
    'product':ProductConfing,
    'default':DevelopConfig
}