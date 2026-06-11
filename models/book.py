class Book:
    def __init__(self, book_id, title, author, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        return self.__dict__