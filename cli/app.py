import argparse
from rich.console import Console

from cli.Display import show_books, show_members, show_loans
from cli.Menus import show_menu
from cli.Prompts import member_prompt, book_prompt, loan_prompt
from services.manager import LibraryManager

console = Console()


def run_cli():
    parser = argparse.ArgumentParser(description="Library Management System")
    subparsers = parser.add_subparsers(dest="command")

    # Register comand name
    subparsers.add_parser("menu")
    subparsers.add_parser("books")
    subparsers.add_parser("members")
    subparsers.add_parser("loans")
    subparsers.add_parser("add-member")
    subparsers.add_parser("add-book")
    subparsers.add_parser("add-loan")

    args = parser.parse_args()

    # Route to the right function based on the command name
    if args.command == "menu":
        show_menu()

    elif args.command == "books":
        manager = LibraryManager()
        show_books(manager.books)

    elif args.command == "members":
        manager = LibraryManager()
        show_members(manager.members)

    elif args.command == "loans":
        manager = LibraryManager()
        show_loans(manager.loans)

    elif args.command == "add-member":
        member_id, name, email = member_prompt()
        manager = LibraryManager()
        member = manager.add_member(member_id, name, email)
        console.print(f"Member added: {member.name} (ID: {member.id})")

    elif args.command == "add-book":
        book_id, title, author, genre, member_id = book_prompt()
        manager = LibraryManager()
        book = manager.add_book(book_id, title, author, genre, member_id)
        console.print(f"Book added: {book.title} (ID: {book.id})")

    elif args.command == "add-loan":
        loan_id, book_id, borrower_id = loan_prompt()
        manager = LibraryManager()
        loan = manager.create_loan(loan_id, book_id, borrower_id)
        console.print(f"Loan created (ID: {loan.id})")

    else:
        parser.print_help()