"""Routes.py"""
from main.models import NETFLIX, netSchema,USERS,users_schema,db
from flask import request, jsonify
from flask import current_app as app
from flask_jwt_extended import create_access_token,jwt_required
from datetime import timedelta

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property  # To deal with ImportError: cannot import name 'cached_property' from 'werkzeug'  when importing flask restplus
import flask.scaffold       # To deal with ImportError: cannot import name '_endpoint_from_view_func' from 'flask.helpers' when importing flask restplus
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restx import Resource,Api, fields


authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}


#Initialising flask Restplus  application with flask app
api = Api(
    app=app,ordered=True,
    title="Netflix Restful API project Documentation",
    description = "This is an Restful which returns netflix movies from a "
                  "PostgreSQL database. To use the API endpoints,"
                  "Please create your profile, then use your credentials to obtain an access token."
                  "Use the access token provided to use the URL endpoints."
                  "Please note: ACCESS TOKENS ARE VALID FOR 5 MINUTES ONLY",
    contact = "Shafiq Kyazze",
    authorizations=authorizations,
    security = 'Bearer Auth'
)



#Model which constructs the expected input fields for the post(create user) request method. It is passed to the api.expect decorator for the post requests
create_user_model = api.model('create_user_model',{
    'username': fields.String('Enter username'),
    'email': fields.String('Enter email'),
    'password': fields.String('Enter password')
})

#Model which constructs the expected input fields for the post(login user) request method
login_user_model = api.model('user_login_model',{
    'username': fields.String('Enter username'),
    'password': fields.String('Enter password ')
})

#Model which constructs the expect input fields for the post(add movie method
add_movie_model = api.model('add_movie_model',{
    'Title': fields.String('Enter movie title'),
    'Genre': fields.String('Enter movie genre'),
    'Premiere': fields.String('Enter movie premiere date'),
    'Run_time' : fields.Float('Enter movie run time'),
    'IMDB_Score': fields.Float('Enter movie IMDB score'),
    'Language' : fields.String('Enter movie original language'),
})


#Schemas to deserialize and serialize data
movie_Scehma = netSchema()
movies_Schema = netSchema(many=True)
USER_SCHEMA= users_schema()


"""URL endpoint that allows users to register their details"""
@api.route("/netflix/user/signup")
class create_user(Resource):
    @api.doc(security=None)
    @api.expect(create_user_model) #tells the function to expect the data in a format similar to the create user model
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        email = data['email']
        if "username" not in data or "password" not in data or "email" not in data: #If the data is input in a non-json format
            return jsonify({"message":"Please fill in all the fields or please input data in a json format"})

        if USERS.check_username(username) is not None:                  #Check to see if username is already in the users database
            return jsonify({"message":'please use a different username'})

        if USERS.check_email(email=data['email']).first() is not None:  #Check to see if email is in the users database
            return jsonify({"message":'please use a different email address'})

        if '@' not in data['email']:  #Verifying email address
            return {"message": "Please enter valid email address"}

        """Inserting items in dictionary after the necessary checks"""
        user_details ={}  #dictionary that contains the items to be stored in the users table
        user_details['login_username'] = username
        non_hashed_password = password
        user_details['email'] = email
        user_details['login_password'] = USERS.generate_hash_password(non_hashed_password) #generating hashed password for the user


        new_user = USER_SCHEMA.load(user_details) #deserialising i.e json to python class
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg":"Your registration was successful"})


"""URL endpoint to allow users to log into the API and receive an access token"""
@api.route("/netflix/user/login")
class login(Resource):
    @api.doc(security=None)
    @api.expect(login_user_model)
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        auth_data = USERS.check_username(username) #data in database with matching username as the input username

        if auth_data is None: #if the user is not in the database
            return {"message":"Username doesn't exist. Please enter valid credentials or sign up for the service"}

        # CHecking to see if hashed version of input password matches the one in the database for the specific username
        if USERS.check_password(auth_data.login_password,password) is True:
            access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=5))  #Give out token that is valid for 5 minutes
            return jsonify({"message":f"{username} your login was successful. Use the access token to make requests","Access Token": f"Bearer {access_token}" })  #Added the word Bearer for the authenticator to understand that Bearer type is a Json Web Token

        #If password check fails
        if USERS.check_password(auth_data.login_password, password) is False:
            return {"message":"Invalid password. Please enter valid information or sign up"}




"""URL endpoint that fetches all the movies in the database"""
@api.route("/netflix/movie/fetchall")
class return_all_movies(Resource):
    @api.doc(params={'Fetch all movies Security Check': {'in': 'header', 'description': 'Access authorization token'}})
    @jwt_required() #ONly authorize user with a valid access token
    def get(self):
        movies = NETFLIX.query.all()
        films = movies_Schema.dump(movies)  #serializing the query results
        return films


"""URL endpoint that fetches a specific movie"""
@api.route("/netflix/movie/fetch")
class get_movie(Resource):
    @api.doc(params={'Fetch single movie Security Check': {'in': 'header', 'description': 'Access authorization token'}})
    @jwt_required()
    def get(self,title):
        movie = NETFLIX.query.filter(NETFLIX.Title == title).first()
        return movie_Scehma.jsonify(movie)


"""URL endpoint that adds a movie to the database"""
@api.route("/netflix/movie/add")
class add_movie(Resource):
    @jwt_required()
    @api.doc(params={'Add specific movie Security Check': {'in': 'header', 'description': 'An authorization token'}})
    @api.expect(add_movie_model)
    def post(self):
        Title = request.json['Title']
        Genre = request.json['Genre']
        Premiere = request.json['Premiere']
        Run_time = request.json['Run_time']
        IMDB_Score = request.json['IMDB_Score']
        Language = request.json['Language']
        if Title or Genre or Premiere or Run_time or IMDB_Score or Language is None:
            return {"message" : "Please fill in all the inputs i.e Title, Genre,Premiere, Run_time, IMDB_Score, Language"}
        new_movie = netSchema(Title, Genre, Premiere, Run_time, IMDB_Score, Language)
        db.session.add(new_movie)
        db.session.commit()
        return movie_Scehma.jsonify(new_movie)


"""Function that deletes movies from the database"""
@api.route("/netflix/movie/delete")
class delete_movie(Resource):
    @api.doc(params={'Delete specific movie Security Check': {'in': 'header', 'description': 'An authorization token'}})
    @jwt_required()
    @api.expect(api.model('delete_model',{'Movie Title': fields.String}))
    def delete(self,title):
        title = request.json['Title']

        if NETFLIX.check_movie_title(title) is not None:
            movie_to_del = NETFLIX.query.get(title)
            db.session.delete(movie_to_del)
            db.commit()
            return movie_Scehma.jsonify(movie_to_del)
        if NETFLIX.check_movie_title(title) is None:
            return {'message': "User not in database"}