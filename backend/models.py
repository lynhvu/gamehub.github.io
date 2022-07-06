from flask import Flask, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
import json
import os

# creating our Flask
api = Flask(__name__, static_folder="../build", static_url_path='/')
CORS(api)

# Not sure about this, but it was in the example
USER = "postgres"
PASSWORD = "abc"
PUBLIC_IP_ADDRESS = "localhost:5432"
DBNAME = "gamehubdb"


api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# needs to be fixed
#api.config['SQLALCHEMY_DATABASE_URI'] = \
os.environ.get("DB_STRING",f'postgresql://{USER}:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}')
# this needs to be fixed still, just put in temp data vv

api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/gamehubdb'

db = SQLAlchemy(api)

# company-games: one to many
# company-genre: many to one
# genre-games: one to many


# Company Model
class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(2000))
    location = db.Column(db.String(200))
    year = db.Column(db.String(50))  # changed this to string because igdb returns timestamps funny
    num_games = db.Column(db.Integer) # replacement for rating
    games = db.relationship('Game', backref='company')
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))  # single main genre for that company
    img = db.Column(db.String(500))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'id': self.id, 
          'name': self.name,
          'description': self.description,
          'location': self.location,
          'year': self.year,
          'num_games': self.num_games,
          'games': self.games,
          'genre_id': self.genre_id,
          'img': self.img
        }

# Game Model


class Game(db.Model):
    __tablename__ = 'game'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(2000))
    score = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    released = db.Column(db.String(50))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    pictures = db.Column(ARRAY(db.String()))
    platforms = db.Column(ARRAY(db.String()))
    
    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'id': self.id, 
          'name': self.name,
          'description': self.description,
          'score': self.score,
          'genre_id': self.genre_id,
          'released': self.released,
          'company_id': self.company_id,
          'pictures': self.pictures,
          'platforms': self.platforms
        }

# Genre Model


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(2000))
    num_games = db.Column(db.Integer)
    games = db.relationship('Game', backref='genre')
    picture = db.Column(db.String(200), nullable = False)
    themes = db.Column(db.String(700))
    companies = db.relationship('Company', backref='genre')

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'id': self.id, 
          'name': self.name,
          'description': self.description,
          'num_games': self.num_games,
          'games': self.games,
          'picture': self.picture,
          'themes': self.themes,
          'companies': self.companies
        }


db.create_all()
