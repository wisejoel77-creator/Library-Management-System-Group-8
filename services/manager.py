from services.datastore import DataStore

class LibraryManager:
    def __init__(self):
        self.store = DataStore()
        self.data = self.store.load()

    def add_book(self, title, author):
        book = {
            "book_id": len(self.data["books"]) + 1,
            "title": title,
            "author": author,
            "status": "available"
        }

        self.data["books"].append(book)
        self.store.save(self.data)
        return "Book added successfully"

    def list_books(self):
        return [
            f"{b['book_id']} - {b['title']} by {b['author']} ({b['status']})"
            for b in self.data["books"]
        ]

    def borrow_book(self, book_id, user_id):
        for book in self.data["books"]:
            if book["book_id"] == book_id:
                if book["status"] == "borrowed":
                    return "Already borrowed"

                book["status"] = "borrowed"
                break
        else:
            return "Book not found"

        loan = {
            "loan_id": len(self.data["loans"]) + 1,
            "book_id": book_id,
            "user_id": user_id,
            "returned": False
        }

        self.data["loans"].append(loan)
        self.store.save(self.data)
        return "Book borrowed"

    def return_book(self, book_id):
        for loan in self.data["loans"]:
            if loan["book_id"] == book_id and not loan["returned"]:
                loan["returned"] = True
                break
        else:
            return "Loan not found"

        for book in self.data["books"]:
            if book["book_id"] == book_id:
                book["status"] = "available"

        self.store.save(self.data)
        return "Book returned"