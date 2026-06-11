# click (used to create commands ie "books", "add-member",)
import click
from rich.console import Console

from cli.Display import show_books, show_members, show_loans
from cli.Menus import show_menu
from cli.Prompts import member_prompt, book_prompt, loan_prompt
from services.manager import LibraryManager

console = Console()

# enables file to have many commands
@click.group()
def run_cli():
    pass

# runs the library-main.py
@run_cli.command()
def menu():
    show_menu()

#LibMan loads data from json
@run_cli.command()
def books():
    manager = LibraryManager()
    show_books(manager.books)

@run_cli.command()
def members():
    manager = LibraryManager()
    show_members(manager.members)

@run_cli.command()
def loans():
    manager = LibraryManager()
    show_loans(manager.loans)

@run_cli.command("add-member")
def add_member():
    member_id, name, email = member_prompt()
    manager = LibraryManager()
    member = manager.add_member(member_id, name, email)
    console.print(f"Member added: {member.name} (ID: {member.id})")


@run_cli.command("add-book")
def add_book():
    book_id, title, author, genre, member_id = book_prompt()
    manager = LibraryManager()
    book = manager.add_book(book_id, title, author, genre, member_id)
    console.print(f"Book added: {book.title} (ID: {book.id})")


@run_cli.command("add-loan")
def add_loan():
    loan_id, book_id, borrower_id = loan_prompt()
    manager = LibraryManager()
    loan = manager.create_loan(loan_id, book_id, borrower_id)
    console.print(f"Loan created (ID: {loan.id})")
