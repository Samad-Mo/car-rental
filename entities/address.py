class Address:
    def __init__(self, number: str, street: str, city: str, postcode: str):
        self.number = number
        self.street = street
        self.city = city
        self.postcode = postcode

    def __str__(self):
        return f'{self.number} {self.street}, {self.city}, {self.postcode}'
