from models.db import db



class Planet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    character = db.relationship('Character', back_populates = 'planet')
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