from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    charachter = db.relationship('Charachter')
    favorites = db.relationship('Favorites')
    
    def __init__(self, population, description, name):
        self.population =  population
        self.description = description
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "population": self.population,
            "name": self.name,
            "description": self.description
            
        }


class Charachter(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    homeWorld = db.Column(db.Integer, db.ForeignKey('planet.id'),nullable=True)
    planet = db.relationship('Planet', back_populates="charachter")
    
    
    def __init__(self, name, description, age, homeWorld):
        self.name =  name
        self.description = description
        self.age = age
        self.homeWorld = homeWorld

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "age": self.age,
            "homeWorld": self.homeWorld   
        }

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    

    def __init__(self, name, last_name, email):
        self.name =  name
        self.last_name = last_name
        self.email = email
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email          
        }

class Favorites(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', back_populates='favorites')
    character_id = db.Column(db.Integer, db.ForeignKey('charachter.id'))
    charachter = db.relationship('Charachter')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    
    def __init__(self, planet_id=None, character_id=None, user_id=None):
        self.planet_id = planet_id
        self.character_id = character_id
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "user_id": self.user_id
        }