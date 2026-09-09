from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from lib.extensions import db
from lib.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if  request.method == 'GET':
        return render_template('auth/register.html')
    elif request.method == 'POST':
        #1
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if not username or len(username) > 20 or not password:
            flash('Enter a username (up to 20 characters) and password')
            return redirect(url_for('auth.register'))
        #2
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        #3
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registered')

        return redirect(url_for('auth.login'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))

        login_user(user)
        flash('Logged in')

        return redirect(url_for('index'))


@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'GET':
        return render_template('auth/logout.html')

    logout_user()
    flash('Logged out')

    return redirect(url_for('index'))
