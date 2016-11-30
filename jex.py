from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.debug = True
app.secret_key = "jex is awesome"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from models import *


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Required: You need to login first.")
            return redirect(url_for('login'))
    return wrap


class EmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])


@app.route('/')
def home():
    form = EmailForm()
    return render_template("index.html", form=form)


@app.route('/signup', methods=['POST'])
def submit_email():
    form = EmailForm()
    if form.validate_on_submit():
        email = request.form['email']
        new_user = User(email)
        db.session.add(new_user)
        db.session.commit()
        flash("Thank you for signing up!")
        return redirect(url_for('home', success=1))
    else:
        flash("Not a valid email address.")
        db.session.rollback()
        return redirect(url_for('home', success=0))


@app.route('/welcome')
# @login_required
def welcome():
    flash("Welcome to Jex!")
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = db.session.query(User).all()

    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['passwd'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash("Success: You have been logged in.")
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error, users=users)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Alert: You have been logged out.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8391
    app.run(host, port)