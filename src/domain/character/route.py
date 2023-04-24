from flask import request, jsonify
from models.index import db, User
import domain.character.controller as Controller 

def character_route(app):

    
    @app.route('/character', methods=['POST'])
    def create_character():
        data = request.get_json()
        character, status=Controller.create_character(data)
        return jsonify(character), status

    @app.route('/character', methods=['GET'])
    def get_characters():
        characters = character.query.all()
        return Controller.get_all_characters(characters)

    @app.route('/character/<int:character_id>', methods=['DELETE'])
    def delete_character(character_id):
        character = character.query.get(character_id)
        return Controller.delete_character()

    @app.route('/character/<int:character_id>', methods=['PUT'])
    def modify_character(character_id):
        character = character.query.get(character_id)
        return Controller.modify_character()