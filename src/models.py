from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref = 'user')


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
            # do not serialize the password, its a security breach
        }

class Favorite(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    planets_id = db.Column(Integer, ForeignKey('planets.id'))
    Characters_id = db.Column(Integer, ForeignKey('characters.id'))
    def __repr__(self):
        return '<Favorite %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": Planets.query.get(self.planets_id).serialize(),
            "characters_id": Characters.query.get(self.characters_id).serialize(),
        }


        
class Planets(db.Model):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    img = db.Column(db.String(120), nullable=False, unique=True)
    climate = db.Column(db.String(120), nullable=False, unique=True)
    gravity = db.Column(db.String(120), nullable=False, unique=True)
    terrain = db.Column(db.String(120), nullable=False, unique=True)
    population = db.Column(db.String(120), nullable=False, unique=True)
    orbital_period = db.Column(db.String(120), nullable=False, unique=True)
    rotation_period = db.Column(db.String(120), nullable=False, unique=True)
    favorites_id = db.relationship('Favorite', backref = 'planets')

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "img": self.img,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period
          }
          
class Characters(db.Model):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    img = db.Column(db.String(120), nullable=False, unique=True)
    height = db.Column(db.String(120), nullable=False, unique=True)
    mass = db.Column(db.String(120), nullable=False, unique=True)
    birth_year = db.Column(db.String(120), nullable=False, unique=True)
    gender = db.Column(db.String(120), nullable=False, unique=True)
    favorites_id = db.relationship('Favorite', backref = 'characters')

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "img": self.img,
            "height": self.height,
            "mass": self.mass,
            "birth_year": self.birth_year,
            "gender": self.gender
            
          }
          