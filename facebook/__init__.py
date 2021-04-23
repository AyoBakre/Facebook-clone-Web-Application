from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_socketio import SocketIO
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db, render_as_batch=True)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
socketio = SocketIO(app)

from facebook import models, routes, errors
