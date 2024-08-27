from flask import render_template, redirect, url_for, flash, request
from app.users import users
from app.users.models import User
from app import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user


# List users

@users.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('users/users.html', users=users)

# Register

@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email already exists
        existing_user_by_email = User.query.filter_by(email=email).first()
        if existing_user_by_email:
            flash('Email address already in use. Please choose a different email.', 'danger')
            return redirect(url_for('users.register'))

        # Check if the username already exists
        existing_user_by_username = User.query.filter_by(username=username).first()
        if existing_user_by_username:
            flash('Username already taken. Please choose a different username.', 'danger')
            return redirect(url_for('users.register'))

        # If neither email nor username exists, create the new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('users.login'))

    return render_template('users/register.html')

# Login

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('admin.index'))  # Redirect to the admin index or any other page
        else:
            flash('Login failed. Check your email and/or password.', 'danger')

    return render_template('users/login.html')

# Logout

@users.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You are now logged out!', 'success')
    return redirect(url_for('users.login'))