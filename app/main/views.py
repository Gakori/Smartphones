from flask import Flask, session
from flask import render_template,request,session,redirect,url_for,request
from . import main
from .. import db

app = Flask(__name__)
app.secret_key="super secret key"

@main.route('/')
def smartphones():
    return render_template('index.html')

        
        
    