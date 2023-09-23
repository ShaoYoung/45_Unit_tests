# notebook

from contact import Contact


class Notebook:
    def __init__(self):
        self.records = []

    def add_contact(self, contact: Contact) -> None:
        self.records.append(contact)

    def find_contact(self, name: str):
        for record in self.records:
            if record.name == name:
                return record
        return None

    def edit_contact(self, contact: Contact, new_name: str, new_phone: str):
        for record in self.records:
            if record.name == contact.name:
                record.name = new_name
                record.phone = new_phone

    def del_contact(self, contact: Contact):
        self.records.remove(contact)

    def __str__(self):
        return '\n'.join([str(record) for record in self.records])
