from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'lana', 'asdf'),
    User(2, 'user2', 'enterasortofpasswordhere'),
    User(3, 'user3', 'enterasortofpasswordhere'),
    User(4, 'user4', 'enterasortofpasswordhere'),
    User(5, 'user5', 'enterasortofpasswordhere'),
    User(6, 'user6', 'enterasortofpasswordhere'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)