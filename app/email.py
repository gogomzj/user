from app import mail
from flask_mail import Message
from threading import Thread
from flask import current_app

def send_fun(app, msg) :
    with app.app_context() :
        mail.send(msg)

def send_mail(subject, recver, html, body) :
    msg = Message(subject=subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[recver])
    msg.body = body
    msg.html = html

    app = current_app._get_current_object()
    thread = Thread(target=send_fun, args=[app, msg])
    thread.start()
