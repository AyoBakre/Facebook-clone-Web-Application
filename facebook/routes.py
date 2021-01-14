from flask import Flask, render_template, url_for, flash, redirect, request
from facebook import app
from facebook.forms import RegistrationForm, LoginForm
from facebook.models import User, Post


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
@app.route("/signup", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    log_form = LoginForm()

    if request.method == 'POST':
        if reg_form.reg_submit.data and reg_form.validate():
            flash(f"Account Successfully Created For {reg_form.fname.data} {reg_form.lname.data}!", "success")
            return redirect(url_for('home'))

        if log_form.log_submit.data and log_form.validate():
            flash(f"Successfully Logged In For {reg_form.fname.data} {reg_form.lname.data}!", "success")
            return redirect(url_for('home'))

        else:
            return render_template('index.html', title='Sign Up | Sign In', reg_form=reg_form, log_form=log_form)
    return render_template('index.html', title='Sign Up | Sign In', reg_form=reg_form, log_form=log_form)


@app.route("/home")
@app.route("/newsfeed")
def home():
    return render_template('home.html', title='Homepage')

