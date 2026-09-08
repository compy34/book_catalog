from cryptography.hazmat.primitives.kdf import scrypt
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
        username = request.form['username']
        password = request.form['password']
        #2
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        #3
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User.create(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registered')

        return redirect(url_for('auth.login'))



def login():
    pass


def logout():
    pass

