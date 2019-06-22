from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='sign-in', form=form)
