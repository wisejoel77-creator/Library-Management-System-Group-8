from models.person import Person

class Member(Person):
    def __init__(self, name, email, membership_id, status="active"):
        super().__init__(name, email)
        self.membership_id = membership_id
        self.status = status

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "membership_id": self.membership_id,
            "status": self.status
        }