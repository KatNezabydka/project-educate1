from Address import Address
from Name import Name
from Birthday import Birthday
from Phone import Phone
from Email import Email


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.addresses = []
        self.birthday = birthday

        if birthday is not None:
            self.birthday = Birthday(birthday)

    def add_phone(self, phone) -> "Record":
        self.phones.append(Phone(phone))

        return self

    def add_email(self, email) -> "Record":
        self.emails.append(Email(email))

        return self

    def add_address(self, address) -> "Record":
        self.addresses.append(Address(address))

        return self

    def delete_phones(self) -> "Record":
        self.phones = []
        return self

    def delete_emails(self) -> "Record":
        self.emails = []
        return self

    def delete_addresses(self) -> "Record":
        self.emails = []
        return self

    def delete_phone(self, phone_for_delete):
        self.phones = [
            phone for phone in self.phones if phone.value != phone_for_delete
        ]

    def delete_email(self, email_for_delete):
        self.emails = [
            email for email in self.emails if email.value != email_for_delete
        ]

    def delete_address(self, address_for_delete):
        self.emails = [
            address for address in self.addresses if address.value != address_for_delete
        ]

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.add_phone(new_phone)

    def edit_email(self, old_email, new_email):
        self.delete_email(old_email)
        self.add_email(new_email)

    def edit_address(self, old_address, new_address):
        self.delete_addresses(old_address)
        self.add_address(new_address)

    def find_phone(self, search_phone):
        for phone in self.phones:
            if phone.value == search_phone:
                return phone.value
        return None

    def print_phones(self) -> str:
        return f"📞 phones: {'; '.join(phone.value for phone in self.phones)}"

    def print_emails(self) -> str:
        if not self.emails:
            return ""
        else:
            return f"📧 emails: {'; '.join(email.value for email in self.emails)}"

    def print_addresses(self) -> str:
        if not self.addresses:
            return ""
        else:
            return f"🏘 address: {'; '.join(address.value for address in self.addresses)}"

    def add_birthday(self, birthday) -> "Record":
        self.birthday = Birthday(birthday)
        return self

    def show_birthday(self):
        print(self.birthday.value.strftime("%d.%m.%Y"))

    def has_birthday(self) -> bool:
        return self.birthday != None

    def __str__(self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday} phones: {'; '.join(phone.value for phone in self.phones)}"
