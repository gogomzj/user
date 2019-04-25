from . import main
from app import db
from flask import render_template
from app.models import User
from flask import session, request

@main.route('/')
def index() :
    #print(session)
    #print(request.cookies)
    return render_template('main/index.html')