import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Loads contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} # Return empty dict if file is empty or corrupted
    else:
        return {}

def save_contacts(contacts):
    """Saves contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """Adds a new contact."""
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if not name or not phone: # Basic validation
        print("Name and phone number are required.")
        return

    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Displays all contacts."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    # Sort contacts by name for better readability
    sorted_names = sorted(contacts.keys())
    
    for name in sorted_names:
        contact_info = contacts[name]
        print(f"Name: {name}")
        print(f"  Phone: {contact_info.get('phone', 'N/A')}")
        print(f"  Email: {contact_info.get('email', 'N/A')}")
        print("-" * 20)

def search_contact(contacts):
    """Searches for contacts by name or phone number."""
    print("\n--- Search Contact ---")
    search_term = input("Enter name or phone number to search: ").strip().lower()
    
    found_contacts = {}
    for name, info in contacts.items():
        if search_term in name.lower() or search_term in info.get('phone', '').lower():
            found_contacts[name] = info
            
    if not found_contacts:
        print("No contacts found matching your search.")
        return

    print("\n--- Search Results ---")
    sorted_names = sorted(found_contacts.keys())
    for name in sorted_names:
        contact_info = found_contacts[name]
        print(f"Name: {name}")
        print(f"  Phone: {contact_info.get('phone', 'N/A')}")
        print(f"  Email: {contact_info.get('email', 'N/A')}")
        print("-" * 20)

def delete_contact(contacts):
    """Deletes a contact."""
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    
    if name_to_delete in contacts:
        confirm = input(f"Are you sure you want to delete '{name_to_delete}'? (yes/no): ").lower()
        if confirm == 'yes':
            del contacts[name_to_delete]
            save_contacts(contacts)
            print(f"Contact '{name_to_delete}' deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Contact '{name_to_delete}' not found.")

def update_contact(contacts):
    """Updates an existing contact's information."""
    print("\n--- Update Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").strip()
    
    if name_to_update in contacts:
        print(f"Updating contact: {name_to_update}")
        print("Enter new details (leave blank to keep current value):")
        
        current_info = contacts[name_to_update]
        
        new_phone = input(f"Enter new phone number (current: {current_info.get('phone', 'N/A')}): ").strip()
        new_email = input(f"Enter new email address (current: {current_info.get('email', 'N/A')}): ").strip()
        
        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email
            
        save_contacts(contacts)
        print(f"Contact '{name_to_update}' updated successfully.")
    else:
        print(f"Contact '{name_to_update}' not found.")

def display_menu():
    """Displays the main menu options."""
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
