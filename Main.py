def display_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    
    # Text file-la details append panroam (a mode)
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
    print("--- Contact added successfully! ---")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("--- No contacts found! ---")
                return
            
            print("\n--- YOUR CONTACTS ---")
            for line in contacts:
                name, phone = line.strip().split(",")
                print(f"Name: {name} | Phone: {phone}")
    except FileNotFoundError:
        print("--- No contacts file found. Add a contact first! ---")

def search_contact():
    search_name = input("Enter Name to Search: ").strip().lower()
    found = False
    
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                if name.lower() == search_name:
                    print(f"\n Found: Name: {name} | Phone: {phone}")
                    found = True
                    break
        if not found:
            print("--- Contact not found! ---")
    except FileNotFoundError:
        print("--- No contacts file found. Add a contact first! ---")

# Main Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Exiting Contact Book. Thank You!")
        break
    else:
        print("Invalid choice! Try again.")
