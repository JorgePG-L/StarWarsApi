from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller 

def planet_route(app):

    
    @app.route('/planet', methods=['POST'])
    def create_planet():
        data = request.get_json()
        planet, status=Controller.create_planet(data)
        return jsonify(planet), status

    @app.route('/planet', methods=['GET'])
    def get_planets():
        planets = Planet.query.all()
        return Controller.get_all_planets(planets)

    @app.route('/planet/<int:planet_id>', methods=['DELETE'])
    def delete_planet(planet_id):
        planet = Planet.query.get(planet_id)
        return Controller.delete_planet()

    @app.route('/planet/<int:planet_id>', methods=['PUT'])
    def modify_planet(planet_id):
        planet = Planet.query.get(planet_id)
        return Controller.modify_planet()