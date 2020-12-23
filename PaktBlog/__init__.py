from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask import Flask

import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_APP_KEY']


db = SQLAlchemy(app)
crypt = Bcrypt(app)
mail = Mail(app)
