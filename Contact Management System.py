import json

contacts = {}

def save_contacts_to_file():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts_from_file():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts_to_file()
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(name):
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts_to_file()
        print(f"Contact '{name}' edited successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts_to_file()
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    global contacts
    contacts = load_contacts_from_file()

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to edit: ")
            edit_contact(name)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

