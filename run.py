from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a secret key change to random later'


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
@app.route("/signup", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    log_form = LoginForm()
    if reg_form.validate_on_submit():
        flash(f"Account Successfully Created For {reg_form.fname.data} {reg_form.lname.data}!", "success")
        return redirect(url_for('home'))
    return render_template('index.html', title='Sign Up | Sign In', reg_form=reg_form, log_form=log_form)


@app.route("/home")
@app.route("/newsfeed")
def home():
    return render_template('home.html', title='Homepage')


if __name__ == '__main__':
    app.run(debug=True)

