import os

phone_book = {
    "Özkan": "5554443322",
    "Ali": "5352223344",
}

def add_contact():  
    name = input("Name:")
    phone = input("Phone:")
    phone_book.update({name: phone})
    print(name, "Added...")
    
def delete_contact():
    name = input("Name:")
    if name in phone_book:
        phone_book.pop(name)
        print(name, "Deleted...")
    else:
        print("User not found.")

def search_contact():
    name = input("Name:")
    if name in phone_book:
        print("Phone Number:", phone_book.get(name))
    else:
        print("User not found.")

def list_contacts():
    print("Name   |   Phone")
    for name, phone in phone_book.items():
        print(name, phone)
    print(len(phone_book), "contacts listed...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Phone Book
    Add    -1
    Search -2
    Delete -3
    List   -4
    """)
    choice = input("Your choice:")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        list_contacts()
    input("Press enter to continue...")
