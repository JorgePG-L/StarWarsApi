from models.index import db, Planet


def create_planet(data):
    new_planet = Planet(data['population'], data['description'], data['name'])
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.serialize()

def get_all_planet(planets):
    
    return jsonify([planet.serialize() for planet in planets]), 200

def delete_user(data):
        db.session.delete(data)
        db.session.commit()
        

def modify_user(data):
    db.session.put(data)
    db.session.commit()
    return ('user modified successfully'), 200