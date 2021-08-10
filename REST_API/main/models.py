"""Model.py"""
from main.init import db
from sqlalchemy import Column
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

#Initialising marshmallow
ma = Marshmallow(db)


class NETFLIX(db.Model):
    """Table called netflix movies constructed"""
    __tablename__ = 'netflix'
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    Title = Column(db.String)
    Genre = Column(db.String)
    Premiere = Column(db.Date)
    Run_time = Column(db.Integer)
    IMDB_Score = Column(db.Float)
    Language = Column(db.String)

    #instantilising data model to ensure all the columns are filled in whening the POST method is called
    def __init__(self,Title, Genre, Premiere, Run_time, IMDB_Score, Language):
        self.Title = Title
        self.Genre = Genre
        self.Premiere = Premiere
        self.Run_time = Run_time
        self.IMDB_Score = IMDB_Score
        self.Language = Language

    # CHecking whether the title exists in the  movie database
    @classmethod
    def check_movie_title(cls, title):
        return cls.query.filter_by(Title = title).first()


"""Schema for table called netflix"""
class netSchema(ma.SQLAlchemyAutoSchema):  #automatic generation of fields from the columns of the table
    class Meta:
        model = NETFLIX   #Model to generate schema from
        load_instance = True #Deserialize/load data to model instance



"""Table to hold the users logging in and out of the Rest API"""
class USERS(db.Model):
    __tablename__ = 'users'
    id= Column(db.Integer, primary_key=True,autoincrement=True)
    login_username = Column(db.String, unique=True, nullable=False)
    login_password = Column(db.String, nullable=False)
    email = Column(db.String,nullable=False)

    def __init__(self,login_username,login_password,email):
        self.login_username = login_username
        self.login_password = login_password
        self.email = email

    #CHecking whether the username exists in the database
    @classmethod
    def check_username(cls,username):
        return cls.query.filter_by(login_username = username).first()

    # CHecking whether the username exists in the database
    @classmethod
    def check_email(cls, login_email):
        return cls.query.filter_by(email = login_email).first()

    #Method that creates hashed passwords
    @staticmethod
    def generate_hash_password(login_passsword):
        return generate_password_hash(login_passsword)

    #Method that checks unhashed password against hashed password
    @staticmethod
    def check_password(password, hashed_password):
        return check_password_hash(password, hashed_password)




class users_schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=USERS
        load_instance = True

#Creating the tables
db.create_all()


