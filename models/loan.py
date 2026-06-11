class Loan:
    def __init__(self, loan_id, book_id, user_id, due_date, returned=False):
        self.loan_id = loan_id
        self.book_id = book_id
        self.user_id = user_id
        self.due_date = due_date
        self.returned = returned

    def to_dict(self):
        return self.__dict__