"""Routes.py"""
from main import app,db
from main.models import NETFLIX, netSchema
from flask import request, jsonify
from config import DATABASE_URI



movie_Scehma = netSchema()
movies_Schema = netSchema(many=True)

#Getting all the movies in the database
@app.route("/allmovies" , methods=["GET"])
def return_all_movies():
    movies = NETFLIX.query.all()
    films = movies_Schema.dump(movies)
    return jsonify(films)

#Getting a single movie in the database
@app.route("/movie/<title>", methods=["GET"])
def get_movie(title):
    movie = NETFLIX.query.filter(NETFLIX.Title == title).first()
    return movie_Scehma.jsonify(movie)

#adding a movie to the database
@app.route("/movie/add", methods=["POST"])
def add_movie():
    Title = request.json['Title']
    Genre = request.json['Genre']
    Premiere = request.json['Premiere']
    Run_time = request.json['Run_time']
    IMDB_Score = request.json['IMDB_Score']
    Language = request.json['Language']

    new_movie = netSchema(Title, Genre, Premiere, Run_time, IMDB_Score, Language)
    db.session.add(new_movie)
    db.session.commit()

    return movie_Scehma.jsonify(new_movie)

#Altering movie
@app.route("/movie/<id>/alter", methods=['PUT'])
def change_movie_details(id):
    movie = NETFLIX.query.get(id)
    Title = request.json['Title']
    Genre = request.json['Genre']
    Premiere = request.json['Premiere']
    Run_time = request.json['Run_time']
    IMDB_Score = request.json['IMDB_Score']
    Language = request.json['Language']

    movie.Title = Title
    movie.Genre = Genre
    movie.Premiere = Premiere
    movie.Run_time = Run_time
    movie.IMDB_Score = IMDB_Score
    movie.Language = Language

    db.session.commit()

    return movie_Scehma.jsonify(movie)


#Deelting movie
@app.route("/movie/<id>/alter", methods=['DELETE'])
def delete_movie(id):
    movie_to_del = NETFLIX.query.get(id)
    db.session.delete(movie_to_del)
    db.commit()

    return movie_Scehma.jsonify(movie_to_del)