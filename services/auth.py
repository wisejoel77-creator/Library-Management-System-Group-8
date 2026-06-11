from utils.security import hash_password

class AuthService:
    def __init__(self, datastore):
        self.datastore = datastore

    def register(self, name, email, password):
        data = self.datastore.load()

        for user in data["users"]:
            if user["email"] == email:
                return "Email already exists"

        user = {
            "user_id": len(data["users"]) + 1,
            "name": name,
            "email": email,
            "password": hash_password(password),
            "role": "user"
        }

        data["users"].append(user)
        self.datastore.save(data)
        return "User registered"

    def login(self, email, password):
        data = self.datastore.load()

        for user in data["users"]:
            if user["email"] == email and user["password"] == hash_password(password):
                return user

        return None