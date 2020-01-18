from flask import Flask, session
from flask import render_template,request,session,redirect,url_for,request
from . import main
from .. import db
from ..models import User, Comment
from flask_login import login_required, current_user
from .forms import commentform

app = Flask(__name__)
app.secret_key="super secret key"

@main.route('/')
def smartphones():
    '''
    route for the index page
    '''
    return render_template('index.html')


@main.route('/iphone')
def iphone():
    '''
    route that navigates to the iphone page
    '''
    return render_template('iphone.html')

@main.route('/sams')
def samsung():
    '''
    route that navigates to the samsung page
    '''
    return render_template('sams.html')


@main.route('/huawei')
def huawei():
    '''
    route that navigates to the huawei page 
    '''
    return render_template('huawei.html')

@main.route('/nokia')
def nokia():
    '''
    route that navigates to the nokia page 
    '''
    return render_template('nokia.html')   
        
@main.route('nokia/comments/<int:id>', methods='GET','POST')
@login_required
def comments(id):
    '''
    route that navigates to the comments page and enables users to comment
    '''
    form = commentform
    user_comment=User.filter_by(id=id).first
    
    if form.validate_on_submit():
            body=form.body.data
            
            new_comment=Comment(body=body, date_posted=date_posted)
            new_comment.save_comment()
            
            return redirect(url_for('.comments',id=id))
        
        comments=Comment.get_comments(id)
    return render_template('comments.html',comments=comments) 
