from datetime import datetime, timedelta

class Loan:
    def __init__(self, book_id, borrower_id, co_borrowers=None, due_days=14, id=None):
        self.id = id         
        self.book_id = book_id
        self.borrower_id = borrower_id
        self.co_borrowers = co_borrowers or []
        self.due_date = str(datetime.now() + timedelta(days=due_days))
        self.returned = False

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        loan = cls(
           book_id =  data["book_id"],
           borrower_id=data["borrower_id"],
           co_borrowers=data.get("co_borrowers", []),
           due_days=data.get("due_days", 14),
           id=data["id"]
            
        )
        loan.due_date = data["due_date"]
        loan.returned = data["returned"]
        return loan