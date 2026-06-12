import click

def get_required_int(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Input cannot be empty. Please enter a value.")
            continue

        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")