from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config_ import DATABASE_URI, jwt_key
from flask_jwt_extended import JWTManager

db = SQLAlchemy() # Initialising sqlalchemy
jwt = JWTManager() #INisitlaising jwt manager

"""Function that constructs and contextualises the flask application"""
def _init_app():
    app = Flask(__name__)  #Initialising the flask application
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI  #Connecting the postgre database to be used by flask
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Turn off event generation
    app.config['JWT_SECRET_KEY'] = jwt_key
    db.init_app(app)   #initialising sqlalchemy on the flask app
    jwt.init_app(app)  #initialising JWT on the flask app


    with app.app_context():
        from main import routes, models
        from main.utils import errors
        return app

