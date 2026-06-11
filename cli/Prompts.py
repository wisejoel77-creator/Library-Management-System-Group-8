def member_prompt():
    return (
        input("Name: "),
        input("Email: ")
    )

def book_prompt():
    return (
        input("Title: "),
        input("Author: "),
        input("Genre: "),
        input("Cataloged by Member ID: ")
    )

def loan_prompt():
    return (
        input("Book ID: "),
        input("Borrower ID: ")
    )