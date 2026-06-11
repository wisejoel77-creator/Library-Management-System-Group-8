#rich(assits in printing dynamic tables in terminal)
from rich.console import Console
from rich.table import Table

#console=>object used to print messages on screen
console = Console()

#create new table, add columns, add rows, print table
def print_table(title, column_names, row_data):
    table = Table(title=title, show_header=True, header_style="bold magenta")
    for name in column_names:
        table.add_column(name)
    for row in row_data:
        table.add_row(*[str(value) for value in row])
    console.print(table)

def show_books(books):
    if not books:
        console.print("No books found")
        return
    
    rows = []
    for book in books:
        rows.append((book.id, book.title, book.author, book.status))
    print_table("Books", ["ID", "Title", "Author", "Status"], rows)

def show_members(members):
    if not members:
        console.print("No members found")
        return
    
    rows = []
    for member in members:
        rows.append((member.id, member.name, member.email))
    print_table("Members", ["ID", "Name", "Email"], rows)

def show_loans(loans):
    if not loans:
        console.print("No loans found")
        return
    
    rows = []
    for loan in loans:
        due = loan.due_date[:10]  # Extract just the date part
        rows.append((loan.id, loan.book_id, loan.borrower_id, due, "Returned" if loan.returned else "Not Returned"))
    print_table("Loans", ["ID", "Book ID", "Borrower ID", "Due Date", "Status"], rows)



















































def show_books(books):
    print("\n--- BOOKS ---")
    for b in books:
        print(f"{b.id} | {b.title} | {b.status}")

def show_members(members):
    print("\n--- MEMBERS ---")
    for m in members:
        print(f"{m.id} | {m.name} | {m.email}")