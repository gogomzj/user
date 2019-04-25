from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import Email, Length, DataRequired, Regexp, EqualTo
from app.models import User
from wtforms import ValidationError

class LoginForm(FlaskForm) :
    email = StringField(label='邮箱',
                        validators=[
                            DataRequired(message='邮箱必须填写'),
                            Length(1, 64, message='邮箱长度必须是1-64'),
                            Email(message='邮箱格式不对')
                        ])
    password = PasswordField(label='密码',
                             validators=[
                                 DataRequired(message='密码必须填写'),
                                 Length(1, 32, message='密码长度必须是1-32'),
                             ])

    remember_me = BooleanField(label='记住我', default=False)
    submit = SubmitField(label='登录')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user is None :
            raise ValidationError('此用户不存在')

class RegisterForm(FlaskForm) :
    email = StringField(label='邮箱',
                        validators=[
                            DataRequired(message='邮箱必须填写'),
                            Length(1, 64, message='邮箱长度必须是1-64'),
                            Email(message='邮箱格式不对')
                        ])
    name = StringField(label='姓名',
                        validators=[
                            DataRequired(message='姓名必须填写'),
                            Length(1, 64, message='姓名长度必须是1-64'),
                        ])
    password = PasswordField(label='密码',
                             validators=[
                                 DataRequired(message='密码必须填写'),
                                 Length(1, 32, message='密码长度必须是1-32'),
                             ])
    password_again = PasswordField(label='确认密码',
                             validators=[
                                 EqualTo('password', message='两次输入的密码不一致')
                             ])

    submit = SubmitField(label='注册')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user :
            raise ValidationError('此用户已经存在')