from flask import Flask
#from flask_mail import Mail
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
#mail = Mail(app)
from app import views, models