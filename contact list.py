
import json

class ContactNumber:
    def __init__(self, number, name):
        self.contact_list = []  # Initialize contact_list as an instance variable
        self.name = name
        self.number = number 

    def save(self):
        # Save the current contact to the list
        self.contact_list.append({'name': self.name, 'number': self.number})
        return f"The contact {self.name} with number {self.number} is saved."

    def add(self):
        # Add the current contact to the list
        self.contact_list.append({'name': self.name, 'number': self.number})
        return f"Contact {self.name} with number {self.number} has been added."

    def backup(self, filename):
        # Save the contact list to a file (for backup)
        with open(filename, 'w') as f:
            for contact in self.contact_list:
                f.write(f"{contact['name']}: {contact['number']}\n")
        return f"Backup successful! Contacts saved to {filename}"

# Example of how to use the class
contact = ContactNumber('123-456-7890', 'John Doe')
print(contact.save())  # Save the first contact
print(contact.add())   # Add the current contact again
print(contact.backup('contacts_backup.txt'))  # Backup contacts to a file
