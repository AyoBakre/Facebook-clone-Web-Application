from flask import render_template, flash, redirect, url_for, request
from facebook import app, db
from facebook.models import User, Post
from facebook.forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
import secrets
import os
from PIL import Image


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/posts', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    posts = Post.query.order_by(Post.timestamp.desc())
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        post_image = save_picture(form.post_image.data)
        post.post_image = post_image
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home Page', form=form, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data, gender=form.gender.data, dob=form.dob.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))