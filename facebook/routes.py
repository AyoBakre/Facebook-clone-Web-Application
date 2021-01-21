from flask import Flask, render_template, url_for, flash, redirect, request
from facebook import app, db, bcrypt
from facebook.forms import RegistrationForm, LoginForm, UpdateProfile
from facebook.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
@app.route("/signup", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    reg_form = RegistrationForm()
    log_form = LoginForm()

    if request.method == 'POST':
        if reg_form.reg_submit.data and reg_form.validate():
            hash_password = bcrypt.generate_password_hash(reg_form.password.data).decode('utf-8')
            user = User(fname=reg_form.fname.data, lname=reg_form.lname.data, email=reg_form.email.data, password=hash_password)
            db.session.add(user)
            db.session.commit()
            flash(f"Account Successfully Created For {reg_form.fname.data} {reg_form.lname.data}!, you can now log in!","success")
            return redirect(url_for('index'))

        if log_form.log_submit.data and log_form.validate():
            user = User.query.filter_by(email=log_form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, log_form.password.data):
                login_user(user, remember=log_form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash(f"login unsuccessful, check your email and password", "danger")

        else:
            return render_template('index.html', title='Sign Up | Sign In', reg_form=reg_form, log_form=log_form)
    return render_template('index.html', title='Sign Up | Sign In', reg_form=reg_form, log_form=log_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/home")
@app.route("/newsfeed")
@login_required
def home():
    return render_template('home.html', title='Homepage')


@app.route("/profile")
@login_required
def profile():
    profile_picture = url_for('static', filename='profile_pics/' + current_user.profile_img_file)
    cover_picture = url_for('static', filename='back_drop_img/' + current_user.cover_img_file)
    bio = current_user.bio
    form = UpdateProfile()
    return render_template('profile.html', title=f" |{current_user.fname} {current_user.lname}", profile_picture=profile_picture, cover_picture=cover_picture, bio=bio, form=form)

