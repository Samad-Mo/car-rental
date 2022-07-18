from car import Car


class Fleet:
    def __init__(self):
        # key: car reg
        # value: car object
        self.cars = {}

        # key: car reg
        # value: person object
        self.rentals = {}

    def add_car(self, car_obj):
        """Add a new car object to the fleet"""

        # add car object to the dictionary
        self.cars[car_obj.reg] = car_obj

    def get_car(self, reg):
        """Get car object from registration number"""

        return self.cars[reg]

    def add_rental(self, reg, person):
        """Log a person renting a car from the fleet"""

        self.rentals[reg] = person
