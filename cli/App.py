from services.manager import LibraryManager

def run_cli():
    manager = LibraryManager()

    while True:
        print("\n===== LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            print(manager.add_book(title, author))

        elif choice == "2":
            books = manager.list_books()
            for b in books:
                print(b)

        elif choice == "3":
            book_id = int(input("Book ID: "))
            user_id = int(input("User ID: "))
            print(manager.borrow_book(book_id, user_id))

        elif choice == "4":
            book_id = int(input("Book ID: "))
            print(manager.return_book(book_id))

        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")