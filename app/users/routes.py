from flask import render_template, redirect, url_for, flash, request
from app.users import users
from app.users.models import User
from app import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user


@users.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('users/users.html', users=users)