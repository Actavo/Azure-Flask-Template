"""
The flask application package.
"""

from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') ## Testing Locally will require entering these or setting in virtual env
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['DEFAULT_MAIL_SENDER'] = 'Admin <engineeringgeofiles@gmail.com>'

mail = Mail(app)

import FlaskWebProject1.views
