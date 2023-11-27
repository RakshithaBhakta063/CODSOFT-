import json

class ContactBook:
    def __init__(self, file_path='contacts.json'):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            self.save_contacts()
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists. Use update to modify.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact {name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            self.save_contacts()
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found. Use add to create a new contact.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter contact name to update: ")
            new_phone = input("Enter new phone number: ")
            contact_book.update_contact(name, new_phone)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
