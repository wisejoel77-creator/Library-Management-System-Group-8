class books:
    def __init__(self, title, author, genre):
        if not author:
            raise ValueError("Author cannot be empty")
        if not genre:
            raise ValueError("Genre cannot be empty")
        self.title = title
        self.author = author
        self.genre = genre