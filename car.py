class Car:
    def __init__(self, reg, make, model, year, mileage, gearbox, fuel_type, seats):
        self.reg = reg
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.gearbox = gearbox
        self.fuel_type = fuel_type
        self.seats = seats

    def __str__(self):
        """Returns a string with all the attribute values"""
        return str(vars(self))
