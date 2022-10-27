from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
import os

local_hash = os.environ.get('APP_SALT')

def generate_password(password, user_salt):
    return generate_password_hash(f'{password}{local_hash}{user_salt}')

def check_password(hash_password, password, user_salt):
    return check_password_hash(hash_password, f'{password}{local_hash}{user_salt}')

def generate_salt():
    return b64encode(os.urandom(32)).decode('utf-8')