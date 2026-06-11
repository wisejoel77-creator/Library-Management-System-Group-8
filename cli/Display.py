def show_books(books):
    print("\n--- BOOKS ---")
    for b in books:
        print(f"{b.id} | {b.title} | {b.status}")

def show_members(members):
    print("\n--- MEMBERS ---")
    for m in members:
        print(f"{m.id} | {m.name} | {m.email}")