from address import Address
from car_fleet import Fleet
from person import Person


def start():
    ahmad = Person('Ahmad', Address(93, 'Romford Road', 'London', 'E15 4HF'))

    fleet = Fleet()
    fleet.add_car('VW19 7BJ', 'Volkswagen', 'Golf', 2019, 70000, 'automatic', 'diesel', 'black', 5)
    fleet.new_rental('VW19 7BJ', ahmad)
    
    # Hello, this is a comment


if __name__ == '__main__':
    start()
