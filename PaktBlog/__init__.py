from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask import Flask

import json
import os

with json.loads(open("environment.json", "r")) as env:
    for key in env:
        os.environ[key] = env['key']

app = Flask(__name__)
app.secret_key = os.environ['FLASK_APP_KEY']


db = SQLAlchemy(app)
crypt = Bcrypt(app)
mail = Mail(app)
