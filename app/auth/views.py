from .forms import LoginForm
from app.models import User
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app import db
from flask import flash

from . import auth
from .forms import RegisterForm


@auth.route('/register', methods=['GET', 'POST'])
def register() :
    form = RegisterForm()
    if form.validate_on_submit() :
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('恭喜【'+user.name+'】注册成功！请登录！')
        return redirect(url_for('.login'))

    return render_template('auth/register.html', form=form)

@auth.route('/logout')
def logout() :
    logout_user()
    return redirect(url_for('.login'))

# 127.0.0.1:5000/login
@auth.route('/login', methods=['GET', 'POST'])
def login() :
    form = LoginForm()
    if form.validate_on_submit() :
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) :
            # 让用户变成登录状态 cookie session
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
        form.email.errors.append('邮箱或者密码错误')

    return render_template('auth/login.html', form=form)