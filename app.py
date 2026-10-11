


# 1. Define the Contact class
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# 2. Define a Node for the Doubly Linked List
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


# 3. Define the Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, contact):
        new_node = Node(contact)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Display contacts from first to last
    def display_forward(self):
        current = self.head

        if current is None:
            print("No contacts found.")
            return

        while current is not None:
            print(f"{current.contact.name} - {current.contact.phone}")
            current = current.next

    # Display contacts from last to first
    def display_backward(self):
        current = self.tail

        if current is None:
            print("No contacts found.")
            return

        while current is not None:
            print(f"{current.contact.name} - {current.contact.phone}")
            current = current.prev


# 4. Define the Contact Manager
class ContactManager:
    def __init__(self):
        self.contacts_list = DoublyLinkedList()
        self.contacts_hash = {}

    # Add a contact to both data structures
    def add_contact(self, name, phone):
        name = name.strip()
        if name.lower() in self.contacts_hash:
            print("A contact with this name already exists.")
            return

        contact = Contact(name, phone)

        self.contacts_list.append(contact)
        self.contacts_hash[name.lower()] = contact

        print("Contact added.")
       
    



    # Search for names containing a keyword using naive matching
    def search_by_keyword(self, keyword):
        current = self.contacts_list.head
        keyword = keyword.lower()
        found = False

        while current is not None:
            name = current.contact.name.lower()

            if self.substring_search(name, keyword):
                print(
                    f"Match found: {current.contact.name} - "
                    f"{current.contact.phone}"
                )
                found = True

            current = current.next

        if not found:
            print("No matching contacts found.")

    # Naive substring search algorithm
    def substring_search(self, text, pattern):
        if pattern == "":
            return True

        for i in range(len(text) - len(pattern) + 1):
            j = 0

            while j < len(pattern) and text[i + j] == pattern[j]:
                j += 1

            if j == len(pattern):
                return True

        return False

    # Search for a contact by exact name using the dictionary
    def search_by_name(self, name):
        contact = self.contacts_hash.get(name.lower())

        if contact is not None:
            print(f"{contact.name} - {contact.phone}")
        else:
            print("Contact not found.")


# 5. Main menu
def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search by Keyword")
        print("3. Search by Exact Name")
        print("4. View All (Forward)")
        print("5. View All (Backward)")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()

            if not name or not phone:
                print("Name and phone cannot be empty.")
            else:
                manager.add_contact(name, phone)

        elif choice == "2":
            keyword = input("Search keyword: ").strip()
            manager.search_by_keyword(keyword)

        elif choice == "3":
            name = input("Enter exact name: ").strip()
            manager.search_by_name(name)

        elif choice == "4":
            manager.contacts_list.display_forward()

        elif choice == "5":
            manager.contacts_list.display_backward()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()