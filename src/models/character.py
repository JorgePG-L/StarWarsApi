from models.db import db


class Character(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'),nullable=True)
    planet = db.relationship('Planet', back_populates = 'character')
    favorites = db.relationship('Favorites')
    
    def __init__(self, name, description, age, homeWorld):
        self.name =  name
        self.description = description
        self.age = age
        self.planet_id = homeWorld

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "age": self.age,
            "homeWorld": self.planet_id   
        }