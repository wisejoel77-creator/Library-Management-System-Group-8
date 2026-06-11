class User:
    def __init__(self, user_id, name, email, password, role="user"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self._password = password
        self.role = role

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)