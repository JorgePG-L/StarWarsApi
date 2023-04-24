import domain.planets.repository as Repository
import handle_response as Response


def create_planet(data):
    if data['population'] is None or data['population'] == '':
        return Response.response_error('population not valid',400)
    if data['description'] is None or data['description'] == '':
        return Response.response_error('description not found',404)
    if data['name'] is None or data['name'] == '':
        return Response.response_error('name not valid',404)
    return Repository.create_planet(data), 201

def get_all_planets(planets):
    
    if planets is None or planets  == '':
        return Response.response_error('list not found',404)
    Repository.get_all_planets(planets)
    return Response.response_ok('planet deleted'),200

def delete_planet(planet_id):
     
    deleted_planet = Repository.delete_planet(planet_id)
    # planet.query.filter(planet.id).delete()
    if deleted_planet is None:
        return Response.response_error('planet not found',404)
    
    return Response.response_ok('planet deleted',200)

def modify_planet(planet_id):
    modified_planet = Repository.modify_planet(planet_id)
    if modified_planet is None :
        return Response.response_error('planet not found',404)
    
    return Response.response_ok('used modified succesfully',200)