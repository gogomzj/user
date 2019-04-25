from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

# flask login要求提供  服务器从session中获取到用户id
# 把id传递个load_user，load_user需要返回用户对象
@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class User(db.Model, UserMixin) :
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.Text)
    location = db.Column(db.String(32))
    head_img_url = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    # 代表用户是否已经激活，如果为True则为激活状态
    confirmed = db.Column(db.Boolean, default=False)

    # 生成token：发送邮件的时候用
    def generate_token(self):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=7200)
        return s.dumps({'id': self.id})

    @property
    def password(self):
        raise AttributeError('密码不可读')

    @password.setter
    def password(self, p):
        # 把用户密码加密后放到password_hash字段 sha256 带杂质串
        self.password_hash = generate_password_hash(p)

    def check_password(self, p):
        return check_password_hash(self.password_hash, p)

