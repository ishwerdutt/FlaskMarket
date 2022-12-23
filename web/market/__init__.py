from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.config import DEV_DB, PROD_DB
import os


app = Flask(__name__)
if os.environ.get('DEBUG') == '1':
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB
app.config['SECRET_KEY'] = 'ebd86588683413c021e72336'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes
