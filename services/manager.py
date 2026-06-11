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

    def add_member(self, member_id, name, email, membership_type="standard"):
        member = Member(member_id, name, email, membership_type)
        self.members.append(member)
        self.persist()
        return member

    def add_book(self, book_id, title, author, genre, member_id):
        book = Book(book_id, title, author, genre, cataloged_by_id=member_id)
        self.books.append(book)
        self.persist()
        return book

    def create_loan(self, loan_id, book_id, borrower_id):
        loan = Loan(loan_id, book_id, borrower_id)
        self.loans.append(loan)
        self.persist()
        return loan