import click


def member_prompt():
        member_id = click.prompt("Member ID"),
        name = click.prompt("Name"),
        email = click.prompt("Email")
        return member_id, name, email


def book_prompt():
        book_id = click.prompt("Book ID"),
        title = click.prompt("Title"),
        author = click.prompt("Author"),
        genre = click.prompt("Genre"),
        member_id = click.prompt("Cataloged by Member ID")
        return book_id, title, author, genre, member_id
    

def loan_prompt():
        loan_id = click.prompt("Loan ID")
        book_id = click.prompt("Book ID")
        borrower_id = click.prompt("Borrower ID")
        return loan_id, book_id, borrower_id
    