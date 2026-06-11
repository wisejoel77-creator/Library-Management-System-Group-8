import click
from rich.console import Console
from rich.panel import Panel

#LibMan handles data loading and saving
from cli.Display import show_books, show_members, show_loans
from cli.Prompts import member_prompt, book_prompt, loan_prompt
from services.manager import LibraryManager

console = Console()

def show_menu():
    manager = LibraryManager()#load lib data from json

    console.print(Panel("Library Management System", style="bold cyan"))#simple title

    #show menu till user chooses 0 to ex
    while True:
        console.print("\n[bold magenta]Menu:[/bold magenta]")
        console.print("1. View Books")
        console.print("2. View Members")
        console.print("3. View Loans")
        console.print("4. Add Member")
        console.print("5. Add Book")
        console.print("6. Add Loan")
        console.print("0. Exit")
        console.print("7. Return a Book")

        choice = click.prompt(
            "Choice",
            type=click.Choice(["0", "1", "2", "3", "4", "5", "6", "7"])
        )

        if choice == "1":
            show_books(manager.books)
        elif choice == "2":
            show_members(manager.members)
        elif choice == "3":
            show_loans(manager.loans)
        elif choice == "4":
            member_id, name, email = member_prompt()
            member = manager.add_member(member_id, name, email)
            console.print(f"Member added: {member.name} (ID: {member.id})")
        elif choice == "5":
            book_id, title, author, genre, member_id = book_prompt()
            book = manager.add_book(book_id, title, author, genre, member_id)
            console.print(f"Book added: {book.title} (ID: {book.id})")
        elif choice == "6":
            loan_id, book_id, borrower_id = loan_prompt()
            loan = manager.create_loan(loan_id, book_id, borrower_id)
            console.print(f"Loan created (ID: {loan.id})")
        
        elif choice == "7":
            member_id = click.prompt("Member ID")
            book_id = click.prompt("Book ID")
            loan, status = manager.return_by_member_and_book(member_id, book_id)

            if status == "success":
               console.print("[green]✓ Loan marked as returned.[/green]")
            elif status == "already_returned":
               console.print("[yellow]This book was already returned.[/yellow]")
            elif status == "not_found":
               console.print("[red]No matching loan found. Double-check the IDs.[/red]")
          
        elif choice == "0":
                console.print("Exiting...")
                break #break loop and end program

               


