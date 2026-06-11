
class Member:
    def __init__(self, id, name, email, membership_type="standard"):
        self.id = id
        self.name = name
        self.email = email
        self.membership_type = membership_type

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.name} ({self.email})"