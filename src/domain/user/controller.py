import domain.user.repository as Repository
import handle_response as Response
from flask import request
from models.index import db, User

def create_user(data):
    if data['email'] is None or data['email'] == '':
        return Response.response_error('email not valid',400)
    if data['name'] is None or data['name'] == '':
        return Response.response_error('name not found',404)
    if data['last_name'] is None or data['last_name'] == '':
        return Response.response_error('last_name not found',404)
    return Repository.create_user(data), 201

def get_all_users(users):

    if users is None:
        return Response.response_error('not users yet',400)
    
    
    return Repository.get_all_users(users)


def delete_user(user):
    if user is None or user == '':
        Response.response_error('user not found',404)
    
    deleted_user = Repository.delete_user(user)  
    return Response.response_ok('user deleted'),200

def modify_user(user):
    
    if user is None:
            return {"message": "El usuario no existe"}, 404
    data = request.get_json()
    if "name" in data is None:
        return Response.response_error('name not found',404)
    if "email" in data is None:
        return Response.response_error('email not found',404)
    if "last_name" in data is None:
        return Response.response_error('last_name not found',404)
    Repository.modify_user(user,data)
    return Response.response_ok('user modified')