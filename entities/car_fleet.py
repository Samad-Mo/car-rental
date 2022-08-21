from entities.car import Car
from entities.person import Person


class Fleet:
    def __init__(self):
        # key: car reg
        # value: car object
        self.cars: dict[str, Car] = {}

        # key: car reg
        # value: person object
        self.rentals: dict[str, Person] = {}

    def add_car(self, car_obj: Car) -> None:
        """Add a new car object to the fleet"""

        # add car object to the dictionary
        self.cars[car_obj.reg] = car_obj

    def get_car(self, reg: str) -> Car:
        """Get car object from registration number"""

        return self.cars[reg]

    def add_rental(self, reg: str, person: Person) -> None:
        """Log a person renting a car from the fleet"""

        self.rentals[reg] = person

    def __str__(self):
        return f'Car fleet with {len(self.cars)} cars and {len(self.rentals)} current rentals'
