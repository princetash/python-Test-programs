from pathlib import Path
import json


def get_stored_user(path):
    """get stored user"""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_user(path):
    """get new user"""
    user = {}
    username = input("What's your name? ")
    email = input("What's your email? ")
    password = input("What's your password? ")
    with open(path, 'w') as file:
        user['username'] = username
        user['email'] = email
        user['password'] = password
        #print(user)
        content = json.dumps(user)
        file.write(content)
        return user
    
get_new_user('username.json')

def greet_user():
    """greets the user with name if he exists"""
    path = Path('username.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back {user['username']}")
        
    else:
        user = get_new_user(path)
        print(f"we will remember you {user['username']}")

greet_user()


