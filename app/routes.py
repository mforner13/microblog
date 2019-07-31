from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Miguel' }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Leeds!'
        },
        {
            'author': {'username': 'Sally'},
            'body': 'Avengers end game was pretty good!'
        },
        {
            'author': {'username': 'Eddy'},
            'body': 'Game of thrones? More like game of unused characterisation!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='sign-in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))