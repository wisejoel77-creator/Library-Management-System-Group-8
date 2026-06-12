import click
from cli.utils import get_required_int

def member_prompt():
        member_id = click.prompt("Member ID", type=str).strip()
        name = click.prompt("Name", type=str).strip()
        email = click.prompt("Email", type=str).strip()
        return member_id, name, email


def book_prompt():
    book_id = click.prompt("Book ID", type=str).strip()
    if not book_id:
        raise ValueError("Book ID cannot be empty.")

    title = click.prompt("Title", type=str).strip()
    if not title:
        raise ValueError("Title cannot be empty.")

    author = click.prompt("Author", type=str).strip()
    if not author:
        raise ValueError("Author cannot be empty.")

    genre = click.prompt("Genre", type=str).strip()
    if not genre:
        raise ValueError("Genre cannot be empty.")

    member_id = click.prompt("Cataloged by Member ID", type=str).strip()
    if not member_id:
        raise ValueError("Member ID cannot be empty.")

    return book_id, title, author, genre, member_id


def loan_prompt():
        loan_id = click.prompt("Loan ID", type=str).strip()
        if not loan_id:
            raise ValueError("Loan ID cannot be empty.")

        book_id = click.prompt("Book ID", type=str).strip()
        if not book_id:
            raise ValueError("Book ID cannot be empty.")

        borrower_id = click.prompt("Borrower ID", type=str).strip()
        if not borrower_id:
            raise ValueError("Borrower ID cannot be empty.")

        return loan_id, book_id, borrower_id
    