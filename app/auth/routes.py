from flask import Blueprint, flash, render_template, redirect, url_for
from app.auth.forms import LoginForm, RegisterForm
from app.extensions import db, bcrypt
from flask_login import login_user, logout_user, login_required
from app.models.user import User

auth= Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        new_user= User(
            username = form.username.data,
            email= form.email.data,
            password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! you can login now')
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('main.home'))
        
        else:
            flash("Somthing went wrong, Check Email and Password", "Danger")
        
    return render_template("auth/login.html", form=form )

@auth.route("/logout")
@login_required
def logout():
        logout_user()
        flash("User Loged out", "info")
        return redirect(url_for('auth.login'))
        