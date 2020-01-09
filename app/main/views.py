from flask import Flask
from flask import render_template,request,session,redirect,url_for,request
from . import main
from .. import db

@main.route('/')
def smartphones():
    return render_template('index.html')

        
        
    