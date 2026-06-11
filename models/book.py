import uuid

class Book:
    def __init__(self, title, author, genre, status="available", cataloged_by_id=None, id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.cataloged_by_id = cataloged_by_id
        self.loan_ids = []

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["title"],
            data["author"],
            data["genre"],
            data["status"],
            data.get("cataloged_by_id"),
            data["id"]
        )
        book.loan_ids = data.get("loan_ids", [])
        return book

    def __str__(self):
        return f"{self.title} by {self.author}"