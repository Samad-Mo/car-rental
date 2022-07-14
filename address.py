class Address:
    def __init__(self, number, street, city, postcode):
        self.number = number
        self.street = street
        self.city = city
        self.postcode = postcode

    def __str__(self):
        return f'{self.number} {self.street}, {self.city}, {self.postcode}'
