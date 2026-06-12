from models.member import Member
from models.book import Book
from models.loan import Loan
from services.datastore import DataStore


class LibraryManager:
    def __init__(self):
        data = DataStore.load()

        self.members = [Member.from_dict(m) for m in data["members"]]
        self.books = [Book.from_dict(b) for b in data["books"]]
        self.loans = [Loan.from_dict(l) for l in data["loans"]]

    def persist(self):
        DataStore.save({
            "members": [m.to_dict() for m in self.members],
            "books": [b.to_dict() for b in self.books],
            "loans": [l.to_dict() for l in self.loans],
        })

    
    def add_member(self, name, email):
        member = Member(name, email)
        self.members.append(member)
        self.persist()
        return member

    def add_book(self, book_id, title, author, genre, member_id):
        if any(str(book.id) == str(book_id) for book in self.books):
            raise ValueError(f"Book ID {book_id} already exists.")
        book = Book(book_id, title, author, genre, cataloged_by_id=member_id)
        self.books.append(book)
        self.persist()
        return book

    
    def create_loan(self, book_id, borrower_id):
        loan = Loan(book_id, borrower_id)
        self.loans.append(loan)
        self.persist()
        return loan
 

    def return_by_member_and_book(self, member_id, book_id):
        for loan in self.loans:
         if loan.borrower_id == member_id and loan.book_id == book_id:
            if loan.returned:
                return None, "already_returned"
            loan.returned = True
            for b in self.books:
                if b.id == book_id:
                    b.status = "available"
            self.persist()
            return loan, "success"
        return None, "not_found"  
