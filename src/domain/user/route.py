from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller 




def user_route(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.get_json()
        user, status=Controller.create_user(data)
        return jsonify(user), status

    @app.route('/user', methods=['GET'])
    def get_user():
        users = User.query.all()
        return Controller.get_all_users(users)

    @app.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        return Controller.delete_user(user)

    @app.route('/user/<int:user_id>', methods=['PUT'])
    def modify_user(user_id):
        user = User.query.filter_by(id=user_id).first()
        return Controller.modify_user(user)