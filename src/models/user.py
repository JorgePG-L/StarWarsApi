from models.db import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    favorites = db.relationship('Favorites')

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