class Car:
    def __init__(
            self,
            reg: str,
            make: str,
            model: str,
            year: int,
            mileage: int,
            gearbox: str,
            fuel_type: str,
            seats: int
    ):
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
