import hashlib

users = {}

def register(email, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    users[email] = hashed

def login(email, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return users.get(email) == hashed