from car import Car


class Fleet:
    def __init__(self):
        # key: car reg
        # value: car object
        self.cars = {}

        # key: car reg
        # value: person object
        self.rentals = {}

    def add_car(self, reg, make, model, year, mileage, gearbox, fuel_type, colour, seats):
        """Adds a new car object to the fleet"""

        # add car object to the dictionary
        self.cars[reg] = Car(reg, make, model, year, mileage, gearbox, fuel_type, colour, seats)

    def new_rental(self, reg, person):
        """Log a person renting a car from the fleet"""

        self.rentals[reg] = person
