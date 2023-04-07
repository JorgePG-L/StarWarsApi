"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Planet, Charachter, User, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/planet', methods=['POST'])
def create_planet():
    body = request.get_json()
    new_planet = Planet(body['population'], body['description'], body['name'])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(new_planet.serialize()), 201

@app.route('/planet', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify({'message': 'Planet deleted successfully'}), 200
    else:
        return jsonify({'error': 'planet not found'}), 404

@app.route('/planet/<int:planet_id>', methods=['PUT'])
def modify_planet(planet_id):
    planet = Planet.query.get(user_id)
    if user:
        db.session.put(planet)
        db.session.commit()
        return jsonify({'message': 'planet modified successfully'}), 200

@app.route('/character', methods=['POST'])
def create_character():
    body = request.get_json()
    new_character = Charachter(body['name'], body['description'], body['age'], body['homeWorld'])
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.serialize()), 201

@app.route('/character', methods=['GET'])
def get_character():
    characters = Charachter.query.all()
    return jsonify([character.serialize() for character in characters]), 200

@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Charachter.query.get(character_id)
    if character:
        db.session.delete(character)
        db.session.commit()
        return jsonify({'message': 'character deleted successfully'}), 200
    else:
        return jsonify({'error': 'character not found'}), 404

@app.route('/character/<int:character_id>', methods=['PUT'])
def modify_character(character_id):
    character = Charachter.query.get(character_id)
    if character:
        db.session.put(character)
        db.session.commit()
        return jsonify({'message': 'character modified successfully'}), 200
    else:
        return jsonify({'error': 'character not found'}), 404

@app.route('/user', methods=['POST'])
def create_user():
    body = request.get_json()
    new_user = User(body['name'], body['last_name'], body['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@app.route('/user', methods=['GET'])
def get_user():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.put(user)
        db.session.commit()
        return jsonify({'message': 'user modified successfully'}), 200

@app.route('/favorites', methods=['POST'])
def create_favorites():
    body = request.get_json()
    new_favorite = Favorites(body['planet_id'], body['character_id'], body['user_id'])
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.serialize()), 201

@app.route('/favorites', methods=['GET'])
def get_favorites():
    favorite = Favorites.query.all()
    return jsonify([favorites.serialize() for favorites in favorite]), 200

    
@app.route('/favorites/<int:favorites_id>', methods=['PUT'])
def modify_favorites(character_id):
    favorites = Favorites.query.get(favorites_id)
    if favorites:
        db.session.put(favorites)
        db.session.commit()
        return jsonify({'message': 'favorites modified successfully'}), 200
    else:
        return jsonify({'error': 'favorites not found'}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
