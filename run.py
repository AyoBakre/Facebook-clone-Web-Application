from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'apsdfmgndkekalke'


@app.route("/")
@app.route("/register")
@app.route("/signup")
@app.route("/login")
def index():
    reg_form = RegistrationForm()
    log_form = LoginForm()
    return render_template('index.html', title='landing page', reg_form=reg_form, log_form=log_form)


@app.route("/home")
@app.route("/newsfeed")
def home():
    return render_template('home.html', title='newsfeed')


if __name__ == '__main__':
    app.run(debug=True)