class Contacts:
    #contacts class with email method

    def __init__(self, first, last, address, phone):
        self.first = first
        self.last = last
        self.adress = address
        self.phone = phone

    def email(self):
        return f'{self.first}{self.last}@email.com'
