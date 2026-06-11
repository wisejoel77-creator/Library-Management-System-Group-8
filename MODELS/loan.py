from datetime import datetime, timedelta
class Loan:
    loan_counter = 0

    def __init__(self, book_id, borrower_id, due_date):
        self.id = Loan.loan_counter
        Loan.loan_counter += 1

        self.book_id = book_id
        self.borrower_id = borrower_id
        self.due_date = due_date
        self.returned = False
    
    def mark_as_returned(self):
        self.returned = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "borrower_id": self.borrower_id,
            "due_date": self.due_date,
            "returned": self.returned
        }
    