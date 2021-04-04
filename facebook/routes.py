from flask import render_template, flash, redirect, url_for
from facebook import app, db
from facebook.models import User
from facebook.forms import RegistrationForm


@app.route('/')
def index():
    return 'Hello world'


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''if current_user.is_authenticated:
        return redirect(url_for('index'))'''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(f_name=form.f_name.data, l_name=form.l_name.data, email=form.email.data, gender=form.gender.data, dob=form.dob.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
