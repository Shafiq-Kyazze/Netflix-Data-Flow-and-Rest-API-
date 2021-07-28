from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

from main import routes, models

