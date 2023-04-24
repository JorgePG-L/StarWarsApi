from models.index import db, User


def create_user(data):
    new_user = User(data['name'], data['last_name'], data['email'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()


def get_all_users(users):
    
    users_data = [user.serialize() for user in users]
    return users_data, 200

def delete_user_favorites(user_id):
    User.query.filter(User.id == 123).delete()
    db.commit()
def delete_user(user):
    db.session.delete(user)
    db.session.commit()
        
def modify_user(user, data):
    
    user.name = data["name"]
    user.email = data["email"]
    user.last_name = data["last_name"]
    db.session.commit()
    
    
    