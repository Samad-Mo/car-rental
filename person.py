class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.total_money = 100
        
    def deduct_money(self, amount):
        self.total_money -= amount

    def __str__(self):
        return f'{self.name} @ {self.address}'