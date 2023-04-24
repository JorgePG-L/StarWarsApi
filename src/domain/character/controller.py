import domain.character.repository as Repository
import handle_response as Response


def create_character(data):
    if data['name'] is None or data['name'] == '':
        return Response.response_error('population not valid',400)
    if data['description'] is None or data['description'] == '':
        return Response.response_error('description not found',404)
    if data['age'] is None or data['age'] == '':
        return Response.response_error('age not valid',404)
    if data['homWorld'] is None or data['homeWorld'] == '':
        return Response.response_error('homeWorld not valid',404)
    return Repository.create_character(data), 201

def get_all_characters(characters):
    
    if characters is None or characters  == '':
        return Response.response_error('list not found',404)
    Repository.get_all_characters(characters)
    return Response.response_ok('character deleted'),200

def delete_character(character_id):
     
    deleted_character = Repository.delete_character(character_id)
    # character.query.filter(character.id).delete()
    if deleted_character is None:
        return Response.response_error('character not found',404)
    
    return Response.response_ok('character deleted',200)

def modify_character(character_id):
    modified_character = Repository.modify_character(character_id)
    if modified_character is None :
        return Response.response_error('character not found',404)
    
    return Response.response_ok('used modified succesfully',200)