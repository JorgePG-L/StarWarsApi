from models.index import db, Character


def create_character(data):
    new_character = Character(data['name'], data['description'], data['homeWorld'])
    db.session.add(new_character)
    db.session.commit()
    return new_character.serialize()

def get_all_character(characters):
    
    return jsonify([character.serialize() for character in characters]), 200

def delete_character(data):
        db.session.delete(data)
        db.session.commit()
        

def modify_character(data):
    db.session.put(data)
    db.session.commit()
    return ('character modified successfully'), 200