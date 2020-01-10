from . import auth 
from flask_login import login_user,logout_user,login_required
from flask import request,render_template,flash,redirect,url_for
from .forms import RegistrationForm, LoginForm

@auth.route('/register', methods =('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.smartphones'))

    return render_template('auth/register.html',form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)