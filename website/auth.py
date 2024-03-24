from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
             flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=password1)
            flash('Account created!', category='success')
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")
